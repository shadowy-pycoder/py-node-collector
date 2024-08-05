from pathlib import Path

import setuptools

setuptools.setup(
    name="py_node_collector",
    version="0.0.3",
    description="Python wrapper for Prometheus Node Collector https://github.com/shadowy-pycoder/go-node-collector",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(include=["py_node_collector"]),
    py_modules=["py_node_collector.collector"],
    package_data={"py_node_collector": ["*.so"]},
    include_package_data=True,
    author="shadowy-pycoder",
    author_email="shadowy-pycoder@example.com",
    platforms="Linux",
    url="https://github.com/shadowy-pycoder/py-node-collector",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    keywords=[
        "prometheus",
        "metrics",
        "prometheus-collector",
        "prometheus-node-exporter",
    ],
)
