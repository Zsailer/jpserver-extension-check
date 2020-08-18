# Jupyter Server Extension Sanity Check

This repo runs a series of Github actions to verify that various jupyter server extensions are discovered and linked to [Jupyter Server]() when installed from the latest release and source. This is critical since Jupyter released Jupyter Server, the new Python server backend, and most of Jupyter's frontend applications will depend on this server.

| Extension | Stable | Latest |
| --------- | -------------- | ------ |
| [jupyterlab](https://github.com/jupyterlab/jupyterlab) | [![jupyterlab](https://github.com/Zsailer/jpserver-extension-check/workflows/jupyterlab-stable/badge.svg)](https://github.com/Zsailer/jpserver-extension-check/actions?query=workflow%3Ajupyterlab-stable) | [![jupyterlab](https://github.com/Zsailer/jpserver-extension-check/workflows/jupyterlab-latest/badge.svg)](https://github.com/Zsailer/jpserver-extension-check/actions?query=workflow%3Ajupyterlab-latest) |
| [nbresuse](https://github.com/yuvipanda/nbresuse) | | [![nbresuse](https://github.com/Zsailer/jpserver-extension-check/workflows/nbresuse/badge.svg)](https://github.com/Zsailer/jpserver-extension-check/actions?query=workflow%3Anbresuse) |
| [nbdime](https://github.com/jupyter/nbdime) | | [![nbdime](https://github.com/Zsailer/jpserver-extension-check/workflows/nbdime/badge.svg)](https://github.com/Zsailer/jpserver-extension-check/actions?query=workflow%3Anbdime) |
| [jupyter-server-proxy](https://github.com/jupyter/jupyter-server-proxy) | | [![jupyter-server-proxy](https://github.com/Zsailer/jpserver-extension-check/workflows/jupyter-server-proxy/badge.svg)](https://github.com/Zsailer/jpserver-extension-check/actions?query=workflow%3Ajupyter-server-proxy) |
| [jupytext](https://github.com/mwouts/jupytext) | | [![jupytext](https://github.com/Zsailer/jpserver-extension-check/workflows/jupytext/badge.svg)](https://github.com/Zsailer/jpserver-extension-check/actions?query=workflow%3Ajupytext) |

Please feel free to add your server extension to the list! Submit a PR with a new set of Github Actions for your extension (you should be able to copy-and-paste the workflow from another extension and change the references to your extension).