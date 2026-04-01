from setuptools import setup
import setup_translate

pkg = 'Extensions.Fempa'
setup(name='enigma2-plugin-extensions-fempa',
       version='3.0',
       description='Norwegian P4 FEM PAA radio show player.',
       package_dir={pkg: 'Fempa'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
