import os
import sys

from hhat_lang import __version__ as hhat_version
from hhat_lang.grammar.cst import parsing_raw_code
from hhat_lang.interpreter.pre_evaluator import PreEvaluator
from hhat_lang.interpreter.evaluator import Evaluator

from ipykernel.kernelbase import Kernel
from ipykernel.kernelapp import IPKernelApp


class HhatKernel(Kernel):
    app_name = "hhat_jupyter_kernel"
    implementation = 'hhat_lang'
    implementation_version = hhat_version
    language = 'H-hat'
    language_version = hhat_version
    banner = 'H-hat is a high level abstraction quantum programming language.'
    language_info = {
        'name': 'hhat_lang',
        'mimetype': 'text/hhat_lang',
        'file_extension': '.hat',
        'pygments_lexer': 'python',
        'version': hhat_version
    }
    kernel_json = {
        "argv": [sys.executable,
                 "-m", "hhat_jupyter_kernel",
                 "-f", "{connection_file}"],
        "display_name": "H-hat",
        "language": "hhat",
        "codemirror_mode": "hhat",
        "name": "hhat_lang"
    }

    content = ""

    def do_execute(self, code, silent=False, store_history=False, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            code_ast = parsing_raw_code(code, False, False, True, False)
            pre_eval = PreEvaluator(code_ast)
            table = pre_eval.walk_tree()
            ev = Evaluator(table, kernel=self)
            ev.run()
        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }


if __name__ == "__main__":
    IPKernelApp.launch_instance(kernel_class=HhatKernel)
