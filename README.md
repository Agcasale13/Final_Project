# met_icon_search

Package that searches the MET and exports icons

## Installation

```bash
$ pip install met_icon_search
```

## Usage

```bash
s=SearchMET()
imgs = s.cropped_images()
print(type(imgs))
print(len(imgs))
print(s.artists())
print(s.objects())
print(s.regions())
print(s.images())
print(s.titles())
s.export_image_icons()
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`met_icon_search` was created by Alex Casale. It is licensed under the terms of the MIT license.

## Credits

`met_icon_search` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
