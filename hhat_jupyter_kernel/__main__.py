from ipykernel.kernelapp import IPKernelApp
from .hhat_kernel import HhatKernel


if __name__ == "__main__":
    IPKernelApp.launch_instance(kernel_class=HhatKernel)

