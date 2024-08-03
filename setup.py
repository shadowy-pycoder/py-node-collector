import setuptools

setuptools.setup(
    name="py_node_collector",
    version="0.0.1",
    description="python wrapper for https://github.com/shadowy-pycoder/go-node-collector",
    packages=setuptools.find_packages(include=["py_node_collector"]),
    py_modules=["py_node_collector.collector"],
    package_data={"py_node_collector": ["*.so"]},
    include_package_data=True,
    author="shadowy-pycoder",
    author_email="shadowy-pycoder@example.com",
    platforms="Linux",
    url="https://github.com/shadowy-pycoder/py-node-collector",
)
