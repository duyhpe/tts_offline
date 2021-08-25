import platform
from setuptools import setup


# Ubuntu: sudo apt install espeak ffmpeg
install_requires = [
    'comtypes; platform_system == "Windows"',
    'pypiwin32; platform_system == "Windows"',
    'pywin32; platform_system == "Windows"',
    'pyobjc>=2.4; platform_system == "Darwin"'
]


with open('README.rst', 'r',encoding='utf-8') as fh:
    long_description = fh.read()


setup(
    name='tts_offline',
    packages=['tts_offline', 'tts_offline.drivers'],
    version='1.0',
    description='Thư viện chuyển đổi văn bản thành giọng nói. Hoạt động Offline, đáp ứng nhanh.',
    long_description=long_description,
    summary='Thư viện chuyển đổi văn bản - giọng nói hỗ trợ đa công cụ',
    author='Edit by Duy.hpe@gmail.com',
    url='https://github.com/duyhpe/tts_offline',
    author_email='duy.hpe@gmail.com',
    install_requires=install_requires ,
    keywords=['pyttsx' , 'ivona','pyttsx for python3' , 'TTS for python3' , 'pyttsx3' ,'text to speech for python','tts','text to speech','speech','speech synthesis','offline text to speech','offline tts','gtts'],
    classifiers = [
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
    ],
)
