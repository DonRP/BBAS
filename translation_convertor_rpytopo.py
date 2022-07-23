from fileinput import FileInput
from glob import glob
import os
import shutil
import re

# ATTENTION: there must not be 2 equal key or value
# regex: https://www.w3schools.com/python/python_regex.asp
dict = {
    # search_text : replace_text
    # start
    r'\\'+'"': r'§§§§§§§§',
    # Effect
    r'" nointeract': r' [nointeract]"',
    r'" with fade': r' [withfade]"',
    r'" with dissolve': r' [withdissolve]"',
    r'" with slowdissolve': r' [withslowdissolve]"',
    r'" with hpunch': r' [withhpunch]"',
    r'" with flash': r' [withflash]"',
    r'" with vpunch': r' [withvpunch]"',
    r'" with Dissolve(2.0)': r' [withDissolve20]"',
    r'    # nvl clear': r'msgid "[nvl_clear]"',
    r'    nvl clear': r'msgstr "[nvl_clear]"',
    # first
    r'    # "(.*?)" "(.*?)"': r'msgid "\1 [special_delimiter] \2"',
    r'    "(.*?)" "(.*?)"': r'msgstr "\1 [special_delimiter] \2"',
    r'    #': r'#',
    r'    old "(.*?)"': r'msgid "\1"',
    r'    new "(.*?)"': r'msgstr "\1"',
    # find:    # (.*?) "(.*?)"
    # replace:msgid "[$1] $2"
    r'# (.*?) "(.*?)"': r'msgid "[\1] \2"',
    # after
    # find:    (.*?) "(.*?)"
    # replace:msgstr "[$1] $2"
    r'    (.*?) "(.*?)"': r'msgstr "[\1] \2"',
    r'# "(.*?)"': r'msgid "\1"',
    r'    "(.*?)"': r'msgstr "\1"',
    # Comment
    r':\n\nmsgid': r':\nmsgid',
    r'rpy:(.*?)\ntranslate': r'rpy:\1 #-#-# translate',
    r'strings:\n\n# ': r'strings: #|#|# # ',
    r'\ntranslate': r'\n#§translate',
    r'updated at (.*?)-(.*?)-(.*?) (.*?):(.*?)\n\n# ': r'updated at \1-\2-\3 \4:\5 #|#|# # ',
    r'(.*?):(.*?)\n\n#§': r'\1:\2 #|#|# #§',
    # end
    r'§§§§§§§§': r'\\'+'"',
}


# Creating a function to replace the text
def replacetext(search_text, replace_text, pathFile):

    # Read in the file
    with open(pathFile, "r+", encoding="utf8") as file:
        filedata = file.read()

    # c = re.compile(search_text)

    # Replace the target string
    # filedata = filedata.replace(search_text, replace_text)
    filedata = re.sub(search_text, replace_text, filedata)
    # TODO: to improve

    # Write the file out again
    with open(pathFile, 'w', encoding="utf8") as file:
        file.write(filedata)
    return True


def replaceDictionary(pathFile, dict={}):
    newpathFile = fileRename(pathFile, extension=".po")
    print(pathFile)
    for search_text in dict.keys():
        replacetext(pathFile=newpathFile, search_text=search_text,
                    replace_text=dict[search_text])
    return


def getListFiles(extension):
    # Get the list of all files and directories
    path = "game/tl/"
    dir_list = glob(path + "/**/*"+extension, recursive=True)
    return dir_list


def rpytopo():
    for path in getListFiles(extension=".rpy"):
        replaceDictionary(path, dict=dict)


def fileRename(pathFile, extension):
    pre, ext = os.path.splitext(pathFile)
    shutil.copyfile(pathFile, pre + extension)
    return pre + extension


rpytopo()
