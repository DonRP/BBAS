from fileinput import FileInput
from glob import glob
import os

# ATTENTION: there must not be 2 equal key or value
dict = {
    # search_text : replace_text
    """
translate crowdin""": """ ## translate crowdin""",
    """    # game""": """# XX## game""",
    """:

    # """: """:
msgid \"""",
    """    old \"""": """msgid  \"""",
    """    new \"""": """msgstr  \"""",
    """\" nointeract""": """ [nointeract]\"""",
    """\" with Dissolve(2.0)""": """ [withDissolve(2.0)]\"""",
    """\n    """: """\nmsgstr \"""",
    # ch
    # Max
    """ \"Max_00 \"""": """ \"[Max_00]""",
    """ \"Max_01 \"""": """ \"[Max_01]""",
    """ \"Max_02 \"""": """ \"[Max_02]""",
    """ \"Max_03 \"""": """ \"[Max_03]""",
    """ \"Max_04 \"""": """ \"[Max_04]""",
    """ \"Max_05 \"""": """ \"[Max_05]""",
    """ \"Max_06 \"""": """ \"[Max_06]""",
    """ \"Max_07 \"""": """ \"[Max_07]""",
    """ \"Max_08 \"""": """ \"[Max_08]""",
    """ \"Max_09 \"""": """ \"[Max_09]""",
    """ \"Max_10 \"""": """ \"[Max_10]""",
    """ \"Max_11 \"""": """ \"[Max_11]""",
    """ \"Max_12 \"""": """ \"[Max_12]""",
    """ \"Max_13 \"""": """ \"[Max_13]""",
    """ \"Max_14 \"""": """ \"[Max_14]""",
    """ \"Max_15 \"""": """ \"[Max_15]""",
    """ \"Max_16 \"""": """ \"[Max_16]""",
    """ \"Max_17 \"""": """ \"[Max_17]""",
    """ \"Max_18 \"""": """ \"[Max_18]""",
    """ \"Max_19 \"""": """ \"[Max_19]""",
    """ \"Max_20 \"""": """ \"[Max_20]""",
    """ \"Max_21 \"""": """ \"[Max_21]""",
    """ \"Max_22 \"""": """ \"[Max_22]""",
    """ \"Max_23 \"""": """ \"[Max_23]""",
    # Ann
    """ \"Ann_00 \"""": """ \"[Ann_00]""",
    """ \"Ann_01 \"""": """ \"[Ann_01]""",
    """ \"Ann_02 \"""": """ \"[Ann_02]""",
    """ \"Ann_03 \"""": """ \"[Ann_03]""",
    """ \"Ann_04 \"""": """ \"[Ann_04]""",
    """ \"Ann_05 \"""": """ \"[Ann_05]""",
    """ \"Ann_06 \"""": """ \"[Ann_06]""",
    """ \"Ann_07 \"""": """ \"[Ann_07]""",
    """ \"Ann_08 \"""": """ \"[Ann_08]""",
    """ \"Ann_09 \"""": """ \"[Ann_09]""",
    """ \"Ann_10 \"""": """ \"[Ann_10]""",
    """ \"Ann_11 \"""": """ \"[Ann_11]""",
    """ \"Ann_12 \"""": """ \"[Ann_12]""",
    """ \"Ann_13 \"""": """ \"[Ann_13]""",
    """ \"Ann_14 \"""": """ \"[Ann_14]""",
    """ \"Ann_15 \"""": """ \"[Ann_15]""",
    """ \"Ann_16 \"""": """ \"[Ann_16]""",
    """ \"Ann_17 \"""": """ \"[Ann_17]""",
    """ \"Ann_18 \"""": """ \"[Ann_18]""",
    """ \"Ann_19 \"""": """ \"[Ann_19]""",
    """ \"Ann_20 \"""": """ \"[Ann_20]""",
    # Eric
    """ \"Eric_00 \"""": """ \"[Eric_00]""",
    """ \"Eric_01 \"""": """ \"[Eric_01]""",
    """ \"Eric_02 \"""": """ \"[Eric_02]""",
    """ \"Eric_03 \"""": """ \"[Eric_03]""",
    """ \"Eric_04 \"""": """ \"[Eric_04]""",
    """ \"Eric_05 \"""": """ \"[Eric_05]""",
    """ \"Eric_06 \"""": """ \"[Eric_06]""",
    """ \"Eric_07 \"""": """ \"[Eric_07]""",
    """ \"Eric_08 \"""": """ \"[Eric_08]""",
    """ \"Eric_09 \"""": """ \"[Eric_09]""",
    """ \"Eric_10 \"""": """ \"[Eric_10]""",
    """ \"Eric_11 \"""": """ \"[Eric_11]""",
    """ \"Eric_12 \"""": """ \"[Eric_12]""",
    """ \"Eric_13 \"""": """ \"[Eric_13]""",
    """ \"Eric_14 \"""": """ \"[Eric_14]""",
    """ \"Eric_15 \"""": """ \"[Eric_15]""",
    """ \"Eric_16 \"""": """ \"[Eric_16]""",
    """ \"Eric_17 \"""": """ \"[Eric_17]""",
    """ \"Eric_18 \"""": """ \"[Eric_18]""",
    """ \"Eric_19 \"""": """ \"[Eric_19]""",
    # Lisa
    """ \"Lisa_00 \"""": """ \"[Lisa_00]""",
    """ \"Lisa_01 \"""": """ \"[Lisa_01]""",
    """ \"Lisa_02 \"""": """ \"[Lisa_02]""",
    """ \"Lisa_03 \"""": """ \"[Lisa_03]""",
    """ \"Lisa_04 \"""": """ \"[Lisa_04]""",
    """ \"Lisa_05 \"""": """ \"[Lisa_05]""",
    """ \"Lisa_06 \"""": """ \"[Lisa_06]""",
    """ \"Lisa_07 \"""": """ \"[Lisa_07]""",
    """ \"Lisa_08 \"""": """ \"[Lisa_08]""",
    """ \"Lisa_09 \"""": """ \"[Lisa_09]""",
    """ \"Lisa_10 \"""": """ \"[Lisa_10]""",
    """ \"Lisa_11 \"""": """ \"[Lisa_11]""",
    """ \"Lisa_12 \"""": """ \"[Lisa_12]""",
    """ \"Lisa_13 \"""": """ \"[Lisa_13]""",
    """ \"Lisa_14 \"""": """ \"[Lisa_14]""",
    """ \"Lisa_15 \"""": """ \"[Lisa_15]""",
    """ \"Lisa_16 \"""": """ \"[Lisa_16]""",
    """ \"Lisa_17 \"""": """ \"[Lisa_17]""",
    """ \"Lisa_18 \"""": """ \"[Lisa_18]""",
    """ \"Lisa_19 \"""": """ \"[Lisa_19]""",
    # Alice
    """ \"Alice_00 \"""": """ \"[Alice_00]""",
    """ \"Alice_01 \"""": """ \"[Alice_01]""",
    """ \"Alice_02 \"""": """ \"[Alice_02]""",
    """ \"Alice_03 \"""": """ \"[Alice_03]""",
    """ \"Alice_04 \"""": """ \"[Alice_04]""",
    """ \"Alice_05 \"""": """ \"[Alice_05]""",
    """ \"Alice_06 \"""": """ \"[Alice_06]""",
    """ \"Alice_07 \"""": """ \"[Alice_07]""",
    """ \"Alice_08 \"""": """ \"[Alice_08]""",
    """ \"Alice_09 \"""": """ \"[Alice_09]""",
    """ \"Alice_10 \"""": """ \"[Alice_10]""",
    """ \"Alice_11 \"""": """ \"[Alice_11]""",
    """ \"Alice_12 \"""": """ \"[Alice_12]""",
    """ \"Alice_13 \"""": """ \"[Alice_13]""",
    """ \"Alice_14 \"""": """ \"[Alice_14]""",
    """ \"Alice_15 \"""": """ \"[Alice_15]""",
    """ \"Alice_16 \"""": """ \"[Alice_16]""",
    """ \"Alice_17 \"""": """ \"[Alice_17]""",
    """ \"Alice_18 \"""": """ \"[Alice_18]""",
    """ \"Alice_19 \"""": """ \"[Alice_19]""",
    # Kira
    """ \"Kira_00 \"""": """ \"[Kira_00]""",
    """ \"Kira_01 \"""": """ \"[Kira_01]""",
    """ \"Kira_02 \"""": """ \"[Kira_02]""",
    """ \"Kira_03 \"""": """ \"[Kira_03]""",
    """ \"Kira_04 \"""": """ \"[Kira_04]""",
    """ \"Kira_05 \"""": """ \"[Kira_05]""",
    """ \"Kira_06 \"""": """ \"[Kira_06]""",
    """ \"Kira_07 \"""": """ \"[Kira_07]""",
    """ \"Kira_08 \"""": """ \"[Kira_08]""",
    """ \"Kira_09 \"""": """ \"[Kira_09]""",
    """ \"Kira_10 \"""": """ \"[Kira_10]""",
    """ \"Kira_11 \"""": """ \"[Kira_11]""",
    """ \"Kira_12 \"""": """ \"[Kira_12]""",
    """ \"Kira_13 \"""": """ \"[Kira_13]""",
    """ \"Kira_14 \"""": """ \"[Kira_14]""",
    """ \"Kira_15 \"""": """ \"[Kira_15]""",
    """ \"Kira_16 \"""": """ \"[Kira_16]""",
    """ \"Kira_17 \"""": """ \"[Kira_17]""",
    """ \"Kira_18 \"""": """ \"[Kira_18]""",
    """ \"Kira_19 \"""": """ \"[Kira_19]""",
    """ \"Kira_20 \"""": """ \"[Kira_20]""",
    # Maya
    """ \"Maya_00 \"""": """ \"[Maya_00]""",
    """ \"Maya_01 \"""": """ \"[Maya_01]""",
    """ \"Maya_02 \"""": """ \"[Maya_02]""",
    """ \"Maya_03 \"""": """ \"[Maya_03]""",
    """ \"Maya_04 \"""": """ \"[Maya_04]""",
    """ \"Maya_05 \"""": """ \"[Maya_05]""",
    """ \"Maya_06 \"""": """ \"[Maya_06]""",
    """ \"Maya_07 \"""": """ \"[Maya_07]""",
    """ \"Maya_08 \"""": """ \"[Maya_08]""",
    """ \"Maya_09 \"""": """ \"[Maya_09]""",
    """ \"Maya_10 \"""": """ \"[Maya_10]""",
    """ \"Maya_11 \"""": """ \"[Maya_11]""",
    """ \"Maya_12 \"""": """ \"[Maya_12]""",
    """ \"Maya_13 \"""": """ \"[Maya_13]""",
    """ \"Maya_14 \"""": """ \"[Maya_14]""",
    """ \"Maya_15 \"""": """ \"[Maya_15]""",
    """ \"Maya_16 \"""": """ \"[Maya_16]""",
    """ \"Maya_17 \"""": """ \"[Maya_17]""",
    """ \"Maya_18 \"""": """ \"[Maya_18]""",
    """ \"Maya_19 \"""": """ \"[Maya_19]""",
    """ \"Maya_20 \"""": """ \"[Maya_20]""",
    """ \"Maya_21 \"""": """ \"[Maya_21]""",
    """ \"Maya_22 \"""": """ \"[Maya_22]""",
    """ \"Maya_23 \"""": """ \"[Maya_23]""",
    # Fix
    """msgstr \"\"[""": """msgstr \"[@""",
    """msgid \"\"[""": """msgid \"[@""",
    #Final
    """\n ## translate crowdin strings:\n\n""": """\n\n# XXtranslate crowdin strings:XX\n""",
    """:XX\n# XX## game""": """:XX# XX## game""",
    # date
    """22:09\n\n# game""": """HH:HH# game""",
    """22:09\n\n# XXtranslate""": """HH:HH# XXtranslate""",
    # only rpytopo
    """msgid \"\"""": """msgid \"""",
    """msgstr \"\"""": """msgstr \"""",
}


# Creating a function to replace the text
def replacetext(search_text, replace_text, pathFile):

    # Read in the file
    with open(pathFile, "r+", encoding="utf8") as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(search_text, replace_text)

    # Write the file out again
    with open(pathFile, 'w', encoding="utf8") as file:
        file.write(filedata)
    return True


def replaceDictionary(pathFile, dict={}, reverse=False):
    print(pathFile)
    if(reverse):
        for item in reversed(list(dict.items())):
            replacetext(pathFile=pathFile,
                        search_text=item[1], replace_text=item[0])
    else:
        for search_text in dict.keys():
            replacetext(pathFile=pathFile, search_text=search_text,
                        replace_text=dict[search_text])


def getListFiles():
    # Get the list of all files and directories
    path = "game/tl/"
    dir_list = glob(path + "/**/*.po", recursive=True)
    return dir_list


def rpytopo():
    for path in getListFiles():
        replaceDictionary(path, dict=dict)


def potorpy():
    for path in getListFiles():
        replaceDictionary(path, dict=dict, reverse=True)


rpytopo()
