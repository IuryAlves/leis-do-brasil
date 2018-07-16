# coding: utf-8

import os
import click
from . import Scraper, get_output_class


click.disable_unicode_literals_warnings = True


@click.command()
@click.argument('urls-file', type=click.File())
@click.option('--output-type', default='file',
              help='The output type of the scraper.'
                   ' Default is to output to a folder')
@click.option('--output-dir',
              type=click.Path(file_okay=False, resolve_path=True),
              default='.',
              help='The output dir when using --output-file=file')
def main(urls_file, output_type, output_dir):

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    urls = urls_file.readlines()
    output_class = get_output_class(output_type)
    output = output_class(output_dir)

    with Scraper(urls, output=output) as scraper:
        scraper.get_contents()


if __name__ == '__main__':
    main()
