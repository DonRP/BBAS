from fileinput import FileInput
from glob import glob
import os

# ATTENTION: there must not be 2 equal key or value
dict = {
    # potorpy only
    """:\n\n    # """: """:\n    # """,
    # not traslate
    """\n# game""": """    new \"\"\n\n# game""",
    # accapo
    """    new \"[""": """    [""",
    """""": """\"
\"""",
    """""": """\"\n\"""",
    """""": """\"\n\"""",
    """    old \"""": """msgid \"""",
    """    new \"""": """    \"""",

    # search_text : replace_text
    """
translate crowdin""": """ ## translate crowdin""",
    """    # game""": """# XX## game""",
    """:
    # """: """:
msgid \"""",
    """\" nointeract""": """ [nointeract]\"""",
    """\" with Dissolve(2.0)""": """ [withDissolve(2.0)]\"""",
    """\n    """: """\nmsgstr \"""",
    # ch
    # Max
    """ \"Max \"""": """ \"[Max] """,
    """ \"Max_00 \"""": """ \"[Max_00] """,
    """ \"Max_01 \"""": """ \"[Max_01] """,
    """ \"Max_02 \"""": """ \"[Max_02] """,
    """ \"Max_03 \"""": """ \"[Max_03] """,
    """ \"Max_04 \"""": """ \"[Max_04] """,
    """ \"Max_05 \"""": """ \"[Max_05] """,
    """ \"Max_06 \"""": """ \"[Max_06] """,
    """ \"Max_07 \"""": """ \"[Max_07] """,
    """ \"Max_08 \"""": """ \"[Max_08] """,
    """ \"Max_09 \"""": """ \"[Max_09] """,
    """ \"Max_10 \"""": """ \"[Max_10] """,
    """ \"Max_11 \"""": """ \"[Max_11] """,
    """ \"Max_12 \"""": """ \"[Max_12] """,
    """ \"Max_13 \"""": """ \"[Max_13] """,
    """ \"Max_14 \"""": """ \"[Max_14] """,
    """ \"Max_15 \"""": """ \"[Max_15] """,
    """ \"Max_16 \"""": """ \"[Max_16] """,
    """ \"Max_17 \"""": """ \"[Max_17] """,
    """ \"Max_18 \"""": """ \"[Max_18] """,
    """ \"Max_19 \"""": """ \"[Max_19] """,
    """ \"Max_20 \"""": """ \"[Max_20] """,
    """ \"Max_21 \"""": """ \"[Max_21] """,
    """ \"Max_22 \"""": """ \"[Max_22] """,
    """ \"Max_23 \"""": """ \"[Max_23] """,
    # Ann
    """ \"Ann \"""": """ \"[Ann] """,
    """ \"Ann_00 \"""": """ \"[Ann_00] """,
    """ \"Ann_01 \"""": """ \"[Ann_01] """,
    """ \"Ann_02 \"""": """ \"[Ann_02] """,
    """ \"Ann_03 \"""": """ \"[Ann_03] """,
    """ \"Ann_04 \"""": """ \"[Ann_04] """,
    """ \"Ann_05 \"""": """ \"[Ann_05] """,
    """ \"Ann_06 \"""": """ \"[Ann_06] """,
    """ \"Ann_07 \"""": """ \"[Ann_07] """,
    """ \"Ann_08 \"""": """ \"[Ann_08] """,
    """ \"Ann_09 \"""": """ \"[Ann_09] """,
    """ \"Ann_10 \"""": """ \"[Ann_10] """,
    """ \"Ann_11 \"""": """ \"[Ann_11] """,
    """ \"Ann_12 \"""": """ \"[Ann_12] """,
    """ \"Ann_13 \"""": """ \"[Ann_13] """,
    """ \"Ann_14 \"""": """ \"[Ann_14] """,
    """ \"Ann_15 \"""": """ \"[Ann_15] """,
    """ \"Ann_16 \"""": """ \"[Ann_16] """,
    """ \"Ann_17 \"""": """ \"[Ann_17] """,
    """ \"Ann_18 \"""": """ \"[Ann_18] """,
    """ \"Ann_19 \"""": """ \"[Ann_19] """,
    """ \"Ann_20 \"""": """ \"[Ann_20] """,
    # Eric
    """ \"Eric \"""": """ \"[Eric] """,
    """ \"Eric_00 \"""": """ \"[Eric_00] """,
    """ \"Eric_01 \"""": """ \"[Eric_01] """,
    """ \"Eric_02 \"""": """ \"[Eric_02] """,
    """ \"Eric_03 \"""": """ \"[Eric_03] """,
    """ \"Eric_04 \"""": """ \"[Eric_04] """,
    """ \"Eric_05 \"""": """ \"[Eric_05] """,
    """ \"Eric_06 \"""": """ \"[Eric_06] """,
    """ \"Eric_07 \"""": """ \"[Eric_07] """,
    """ \"Eric_08 \"""": """ \"[Eric_08] """,
    """ \"Eric_09 \"""": """ \"[Eric_09] """,
    """ \"Eric_10 \"""": """ \"[Eric_10] """,
    """ \"Eric_11 \"""": """ \"[Eric_11] """,
    """ \"Eric_12 \"""": """ \"[Eric_12] """,
    """ \"Eric_13 \"""": """ \"[Eric_13] """,
    """ \"Eric_14 \"""": """ \"[Eric_14] """,
    """ \"Eric_15 \"""": """ \"[Eric_15] """,
    """ \"Eric_16 \"""": """ \"[Eric_16] """,
    """ \"Eric_17 \"""": """ \"[Eric_17] """,
    """ \"Eric_18 \"""": """ \"[Eric_18] """,
    """ \"Eric_19 \"""": """ \"[Eric_19] """,
    # Lisa
    """ \"Lisa \"""": """ \"[Lisa] """,
    """ \"Lisa_00 \"""": """ \"[Lisa_00] """,
    """ \"Lisa_01 \"""": """ \"[Lisa_01] """,
    """ \"Lisa_02 \"""": """ \"[Lisa_02] """,
    """ \"Lisa_03 \"""": """ \"[Lisa_03] """,
    """ \"Lisa_04 \"""": """ \"[Lisa_04] """,
    """ \"Lisa_05 \"""": """ \"[Lisa_05] """,
    """ \"Lisa_06 \"""": """ \"[Lisa_06] """,
    """ \"Lisa_07 \"""": """ \"[Lisa_07] """,
    """ \"Lisa_08 \"""": """ \"[Lisa_08] """,
    """ \"Lisa_09 \"""": """ \"[Lisa_09] """,
    """ \"Lisa_10 \"""": """ \"[Lisa_10] """,
    """ \"Lisa_11 \"""": """ \"[Lisa_11] """,
    """ \"Lisa_12 \"""": """ \"[Lisa_12] """,
    """ \"Lisa_13 \"""": """ \"[Lisa_13] """,
    """ \"Lisa_14 \"""": """ \"[Lisa_14] """,
    """ \"Lisa_15 \"""": """ \"[Lisa_15] """,
    """ \"Lisa_16 \"""": """ \"[Lisa_16] """,
    """ \"Lisa_17 \"""": """ \"[Lisa_17] """,
    """ \"Lisa_18 \"""": """ \"[Lisa_18] """,
    """ \"Lisa_19 \"""": """ \"[Lisa_19] """,
    # Alice
    """ \"Alice \"""": """ \"[Alice] """,
    """ \"Alice_00 \"""": """ \"[Alice_00] """,
    """ \"Alice_01 \"""": """ \"[Alice_01] """,
    """ \"Alice_02 \"""": """ \"[Alice_02] """,
    """ \"Alice_03 \"""": """ \"[Alice_03] """,
    """ \"Alice_04 \"""": """ \"[Alice_04] """,
    """ \"Alice_05 \"""": """ \"[Alice_05] """,
    """ \"Alice_06 \"""": """ \"[Alice_06] """,
    """ \"Alice_07 \"""": """ \"[Alice_07] """,
    """ \"Alice_08 \"""": """ \"[Alice_08] """,
    """ \"Alice_09 \"""": """ \"[Alice_09] """,
    """ \"Alice_10 \"""": """ \"[Alice_10] """,
    """ \"Alice_11 \"""": """ \"[Alice_11] """,
    """ \"Alice_12 \"""": """ \"[Alice_12] """,
    """ \"Alice_13 \"""": """ \"[Alice_13] """,
    """ \"Alice_14 \"""": """ \"[Alice_14] """,
    """ \"Alice_15 \"""": """ \"[Alice_15] """,
    """ \"Alice_16 \"""": """ \"[Alice_16] """,
    """ \"Alice_17 \"""": """ \"[Alice_17] """,
    """ \"Alice_18 \"""": """ \"[Alice_18] """,
    """ \"Alice_19 \"""": """ \"[Alice_19] """,
    # Kira
    """ \"Kira \"""": """ \"[Kira] """,
    """ \"Kira_00 \"""": """ \"[Kira_00] """,
    """ \"Kira_01 \"""": """ \"[Kira_01] """,
    """ \"Kira_02 \"""": """ \"[Kira_02] """,
    """ \"Kira_03 \"""": """ \"[Kira_03] """,
    """ \"Kira_04 \"""": """ \"[Kira_04] """,
    """ \"Kira_05 \"""": """ \"[Kira_05] """,
    """ \"Kira_06 \"""": """ \"[Kira_06] """,
    """ \"Kira_07 \"""": """ \"[Kira_07] """,
    """ \"Kira_08 \"""": """ \"[Kira_08] """,
    """ \"Kira_09 \"""": """ \"[Kira_09] """,
    """ \"Kira_10 \"""": """ \"[Kira_10] """,
    """ \"Kira_11 \"""": """ \"[Kira_11] """,
    """ \"Kira_12 \"""": """ \"[Kira_12] """,
    """ \"Kira_13 \"""": """ \"[Kira_13] """,
    """ \"Kira_14 \"""": """ \"[Kira_14] """,
    """ \"Kira_15 \"""": """ \"[Kira_15] """,
    """ \"Kira_16 \"""": """ \"[Kira_16] """,
    """ \"Kira_17 \"""": """ \"[Kira_17] """,
    """ \"Kira_18 \"""": """ \"[Kira_18] """,
    """ \"Kira_19 \"""": """ \"[Kira_19] """,
    """ \"Kira_20 \"""": """ \"[Kira_20] """,
    # Maya
    """ \"Maya \"""": """ \"[Maya] """,
    """ \"Maya_00 \"""": """ \"[Maya_00] """,
    """ \"Maya_01 \"""": """ \"[Maya_01] """,
    """ \"Maya_02 \"""": """ \"[Maya_02] """,
    """ \"Maya_03 \"""": """ \"[Maya_03] """,
    """ \"Maya_04 \"""": """ \"[Maya_04] """,
    """ \"Maya_05 \"""": """ \"[Maya_05] """,
    """ \"Maya_06 \"""": """ \"[Maya_06] """,
    """ \"Maya_07 \"""": """ \"[Maya_07] """,
    """ \"Maya_08 \"""": """ \"[Maya_08] """,
    """ \"Maya_09 \"""": """ \"[Maya_09] """,
    """ \"Maya_10 \"""": """ \"[Maya_10] """,
    """ \"Maya_11 \"""": """ \"[Maya_11] """,
    """ \"Maya_12 \"""": """ \"[Maya_12] """,
    """ \"Maya_13 \"""": """ \"[Maya_13] """,
    """ \"Maya_14 \"""": """ \"[Maya_14] """,
    """ \"Maya_15 \"""": """ \"[Maya_15] """,
    """ \"Maya_16 \"""": """ \"[Maya_16] """,
    """ \"Maya_17 \"""": """ \"[Maya_17] """,
    """ \"Maya_18 \"""": """ \"[Maya_18] """,
    """ \"Maya_19 \"""": """ \"[Maya_19] """,
    """ \"Maya_20 \"""": """ \"[Maya_20] """,
    """ \"Maya_21 \"""": """ \"[Maya_21] """,
    """ \"Maya_22 \"""": """ \"[Maya_22] """,
    """ \"Maya_23 \"""": """ \"[Maya_23] """,
    # Olivia
    """ \"Olivia \"""": """ \"[Olivia] """,
    """ \"Olivia_00 \"""": """ \"[Olivia_00] """,
    """ \"Olivia_01 \"""": """ \"[Olivia_01] """,
    """ \"Olivia_02 \"""": """ \"[Olivia_02] """,
    """ \"Olivia_03 \"""": """ \"[Olivia_03] """,
    """ \"Olivia_04 \"""": """ \"[Olivia_04] """,
    """ \"Olivia_05 \"""": """ \"[Olivia_05] """,
    """ \"Olivia_06 \"""": """ \"[Olivia_06] """,
    """ \"Olivia_07 \"""": """ \"[Olivia_07] """,
    """ \"Olivia_08 \"""": """ \"[Olivia_08] """,
    """ \"Olivia_09 \"""": """ \"[Olivia_09] """,
    """ \"Olivia_10 \"""": """ \"[Olivia_10] """,
    """ \"Olivia_11 \"""": """ \"[Olivia_11] """,
    """ \"Olivia_12 \"""": """ \"[Olivia_12] """,
    """ \"Olivia_13 \"""": """ \"[Olivia_13] """,
    """ \"Olivia_14 \"""": """ \"[Olivia_14] """,
    """ \"Olivia_15 \"""": """ \"[Olivia_15] """,
    """ \"Olivia_16 \"""": """ \"[Olivia_16] """,
    """ \"Olivia_17 \"""": """ \"[Olivia_17] """,
    """ \"Olivia_18 \"""": """ \"[Olivia_18] """,
    """ \"Olivia_19 \"""": """ \"[Olivia_19] """,
    """ \"Olivia_20 \"""": """ \"[Olivia_20] """,
    """ \"Olivia_21 \"""": """ \"[Olivia_21] """,
    """ \"Olivia_22 \"""": """ \"[Olivia_22] """,
    """ \"Olivia_23 \"""": """ \"[Olivia_23] """,
    # Christine
    """ \"Christine \"""": """ \"[Christine] """,
    """ \"Christine_00 \"""": """ \"[Christine_00] """,
    """ \"Christine_01 \"""": """ \"[Christine_01] """,
    """ \"Christine_02 \"""": """ \"[Christine_02] """,
    """ \"Christine_03 \"""": """ \"[Christine_03] """,
    """ \"Christine_04 \"""": """ \"[Christine_04] """,
    """ \"Christine_05 \"""": """ \"[Christine_05] """,
    """ \"Christine_06 \"""": """ \"[Christine_06] """,
    """ \"Christine_07 \"""": """ \"[Christine_07] """,
    """ \"Christine_08 \"""": """ \"[Christine_08] """,
    """ \"Christine_09 \"""": """ \"[Christine_09] """,
    """ \"Christine_10 \"""": """ \"[Christine_10] """,
    """ \"Christine_11 \"""": """ \"[Christine_11] """,
    """ \"Christine_12 \"""": """ \"[Christine_12] """,
    """ \"Christine_13 \"""": """ \"[Christine_13] """,
    """ \"Christine_14 \"""": """ \"[Christine_14] """,
    """ \"Christine_15 \"""": """ \"[Christine_15] """,
    """ \"Christine_16 \"""": """ \"[Christine_16] """,
    """ \"Christine_17 \"""": """ \"[Christine_17] """,
    """ \"Christine_18 \"""": """ \"[Christine_18] """,
    """ \"Christine_19 \"""": """ \"[Christine_19] """,
    """ \"Christine_20 \"""": """ \"[Christine_20] """,
    """ \"Christine_21 \"""": """ \"[Christine_21] """,
    """ \"Christine_22 \"""": """ \"[Christine_22] """,
    """ \"Christine_23 \"""": """ \"[Christine_23] """,
    # Sam
    """ \"Sam \"""": """ \"[Sam] """,
    """ \"Sam_00 \"""": """ \"[Sam_00] """,
    """ \"Sam_01 \"""": """ \"[Sam_01] """,
    """ \"Sam_02 \"""": """ \"[Sam_02] """,
    """ \"Sam_03 \"""": """ \"[Sam_03] """,
    """ \"Sam_04 \"""": """ \"[Sam_04] """,
    """ \"Sam_05 \"""": """ \"[Sam_05] """,
    """ \"Sam_06 \"""": """ \"[Sam_06] """,
    """ \"Sam_07 \"""": """ \"[Sam_07] """,
    """ \"Sam_08 \"""": """ \"[Sam_08] """,
    """ \"Sam_09 \"""": """ \"[Sam_09] """,
    """ \"Sam_10 \"""": """ \"[Sam_10] """,
    """ \"Sam_11 \"""": """ \"[Sam_11] """,
    """ \"Sam_12 \"""": """ \"[Sam_12] """,
    """ \"Sam_13 \"""": """ \"[Sam_13] """,
    """ \"Sam_14 \"""": """ \"[Sam_14] """,
    """ \"Sam_15 \"""": """ \"[Sam_15] """,
    """ \"Sam_16 \"""": """ \"[Sam_16] """,
    """ \"Sam_17 \"""": """ \"[Sam_17] """,
    """ \"Sam_18 \"""": """ \"[Sam_18] """,
    """ \"Sam_19 \"""": """ \"[Sam_19] """,
    """ \"Sam_20 \"""": """ \"[Sam_20] """,
    """ \"Sam_21 \"""": """ \"[Sam_21] """,
    """ \"Sam_22 \"""": """ \"[Sam_22] """,
    """ \"Sam_23 \"""": """ \"[Sam_23] """,

    """ \"extend \"""": """ \"[extend] """,
    # Fix
    """msgstr \"\"[""": """msgstr \"[@""",
    """msgid \"\"[""": """msgid \"[@""",
    #Final
    """\n ## translate crowdin strings:\n\n""": """\n\n# XXtranslate crowdin strings:XX\n""",
    """:XX\n# XX## game""": """:XX# XX## game""",
    # date
    """HH:HH\n\n# game""": """HH:HH# game""",
    """HH:HH\n\n# XXtranslate""": """HH:HH# XXtranslate""",
    # potorpy only
    """msgstr \"[""": """msgstr \"\"[""",
    """msgstr \"\"""": """msgstr \"""",
    """""": """msgstr \"\"""",
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
    dir_list = glob(path + "/**/*.rpy", recursive=True)
    return dir_list


def rpytopo():
    for path in getListFiles():
        replaceDictionary(path, dict=dict)


def potorpy():
    for path in getListFiles():
        replaceDictionary(path, dict=dict, reverse=True)


potorpy()
