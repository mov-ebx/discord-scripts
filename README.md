<div align="center">
    <h1><img src="https://assets-global.website-files.com/6257adef93867e50d84d30e2/636e0a6ca814282eca7172c6_icon_clyde_white_RGB.svg"width="30px"><br>Discord Scripts/Multi-Tool</h1>
    <img src="https://i.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif">
    <h3>Collection of scripts written by me for the Discord platform</h3>
    <h5>[WARNING]<br>While I did my best to make these undetectable, you may get terminated from Discord as this violates their ToS</h5>

[![Python 3.10](https://img.shields.io/badge/Python-3.10-bluesvg)](https://www.python.org/download/releases/3.0/)
[![GitHub license](https://img.shields.io/badge/license-GPL%202.0-green)](./LICENSE)
</div>

## How do you use the scripts?

While you can use each script indivdually in the [scripts directory](src/scripts/), the easiest way to use the scripts, is by using the launcher. The launcher is available in the "Releases" tab.

All you need is Python installed and the necessary [requirements](src/requirements.txt). I wrote the scripts in Python 3.10.6, so I'd recommend you [install that version](https://www.python.org/downloads/release/python-3106/). However, later versions should work too.

## How can I integrate the scripts in my projects?

You can easily integrate the scripts in your project, just make sure to follow the [license](LICENSE)!

Each script has a function inside of it called "run" which can be called with the necessary parameters.

Here's an example on how to integrate an example script in your project:

```py
import scripts.example
example.run("token", "other parameter")
```

There is also a dictionary in all the scripts which has all the parameters, along with a string which has the description:

```py
import scripts.example
print(example.params) # Parameters
print(example.desc) # Description
```
