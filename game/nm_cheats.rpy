init 1:
    screen menu_inventory():
        add 'interface phon2'
        style_prefix 'inventory' tag menu

        grid 2 1:
            xpos 0.2 ypos 0.02 spacing 50
            vbox:   # Speedy delivery
                imagebutton:
                    idle im.Scale ("images/interface/wait_60.webp",90,90)
                    hover im.Scale ("images/interface/wait_60.webp",95,95)
                    action [
                                GetDeliveryList(),
                                If(len(delivery_list[0])>0, true=Jump('delivery1')),
                                If(len(delivery_list[1])>0, true=Jump('delivery2'))
                        ]
                text _("Speedy Delivery") xcenter 0.25 color gui.accent_color size 28 font "hermes.ttf"

            vbox: # Catch a spider
                if poss['spider'].st() >= 1:
                    if items['spider'].have == False:
                        imagebutton:
                            idle im.Scale ("images/interface/spider.webp",90,90)
                            hover im.Scale ("images/interface/spider.webp",95,95)
                            action Function(australian_mode)
                        text _("Australian mode: On") xcenter 0.20 color gui.accent_color size 28 font "hermes.ttf"
                else:
                    null

        frame area (150, 95, 350, 50) background None:
            text _("ВЕЩИ") color gui.accent_color size 28 font 'hermes.ttf'

        imagebutton pos (1740, 100) auto 'interface close %s' action Jump('AfterWaiting'):
            if not renpy.variant('small'):
                focus_mask True
            at close_zoom

        $ cells = 0
        $ items_list = {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            4 : []
        }
        $ listrows = [0, 0, 0, 0, 0]

        $ cur_col = 0
        for id in items:
            if items[id].have:
                $ cells += items[id].cells
                if items[id].cells > 1:
                    $ listrows[cur_col] += items[id].cells
                    $ items_list[cur_col].append(id)
                    $ cur_col += 1
                    if cur_col > 4:
                        $ cur_col = 1


        if cells % 5 > 0:
            $ tabrows = cells // 5 + 1
        else:
            $ tabrows = cells // 5

        for id in items:
            if items[id].have and items[id].cells == 1:
                $ cur_col = 5
                for i in range(5):
                    if cur_col == 5 and listrows[i] == min(listrows):
                        $ cur_col = i

                $ added = False
                if listrows[cur_col] + items[id].cells <= tabrows:
                    $ added = True
                    $ listrows[cur_col] += items[id].cells
                    $ items_list[cur_col].append(id)

        if cells > 0:
            $ desc = _("Ни один предмет не выбран")
        else:
            $ desc = _("В данный момент в инвентаре ничего нет")

        default tl = Tooltip("")
        default tdesc = Tooltip(desc)

        vbox:
            xalign 0.5
            xsize 1620
            ypos 170
            spacing 15
            frame xsize 1460 ysize 650 xalign 0.5 background None:
                has viewport:
                    xalign 0.5
                    draggable True
                    mousewheel True
                if tabrows > 2:
                    scrollbars 'vertical'

                if tabrows < 3:
                    $ tabrows = 3
                hbox:
                    spacing 2
                    for cur_col in range(5):
                        vbox:
                            spacing 4
                            for id in items_list[cur_col]:
                                $ im_name = 'interface/items/' + items[id].img + '.webp'
                                if items[id].cells == 2:
                                    frame area (0, 0, 286, 456) background 'interface items bg2':
                                        imagebutton align (0.5, 0.5) idle 'interface items '+items[id].img action NullAction() at things:
                                            hovered [tl.Action(items[id].name), tdesc.Action(items[id].desc)]
                                else:
                                    frame area (0, 0, 286, 226) background 'interface items bg':
                                        imagebutton align (0.5, 0.5) idle 'interface items '+items[id].img action NullAction() at things:
                                            hovered [tl.Action(items[id].name), tdesc.Action(items[id].desc)]

                            $ addcells = tabrows - listrows[cur_col]
                            if addcells > 0:
                                for i in range(addcells):
                                    frame area (0, 0, 286, 226) background 'interface items bg':
                                        button align (0.5, 0.5) action NullAction():
                                            hovered [tl.Action(''), tdesc.Action(desc)]


            frame area (200, 0, 1220, 50) background None:
                text tl.value xalign 0.5 size 28 font 'hermes.ttf' color gui.text_color

            frame area (300, 0, 1020, 180) background None:
                text tdesc.value xalign 0.5 size gui.text_size font gui.text_font color gui.accent_color

        key 'K_ESCAPE' action Jump('AfterWaiting')
        key 'mouseup_3' action Jump('AfterWaiting')


    screen menu_userinfo():


        add 'interface phon'
        style_prefix 'userinfo' tag menu

        frame area (150, 95, 350, 50) background None:
            text _("ПЕРСОНАЖИ") color gui.accent_color size 28 font 'hermes.ttf'

        imagebutton pos (1740, 100) auto 'interface close %s' action Jump('AfterWaiting'):
            if not renpy.variant('small'):
                focus_mask True
            at close_zoom

        hbox pos (150, 150) spacing 30:
            hbox ypos 25 xsize 190 spacing 5:
                viewport mousewheel 'change' draggable True id 'vp':
                    has vbox spacing 5
                    button background None action SetVariable('CurChar', 'max') xsize 180:

                        textbutton _("Макс") action SetVariable('CurChar', 'max') selected CurChar == 'max' text_selected_color gui.text_color
                        foreground 'interface marker'
                    for char in sorted(chars.keys()):
                        button background None action SetVariable('CurChar', char) xsize 180:

                            textbutton chars[char].name action SetVariable('CurChar', char) selected CurChar == char text_selected_color gui.text_color
                            foreground 'interface marker'
                vbar value YScrollValue('vp') style 'info_vscroll'

            if CurChar == 'max':
                add 'Max info '+mgg.clothes.casual.GetCur().info size (550, 900) xpos -50 ypos 10

            else:
                frame xysize (550, 900) background None:
                    if chars[CurChar].dress_inf == '':
                        add chars[CurChar].pref+' info-00' size (550, 900) xpos -50 ypos 10
                    else:
                        add chars[CurChar].pref+' info '+chars[CurChar].dress_inf size (550, 900) xpos -50 ypos 10

            viewport area (0, 30, 880, 800):
                has vbox spacing 20
                frame xsize 850 background None:
                    if CurChar == 'max':
                        text mgg.desc size 24 justify True first_indent 30
                    else:
                        text renpy.config.say_menu_text_filter(renpy.translate_string(chars[CurChar].desc)) size 24 justify True


                hbox pos (20, 0) xsize 810 spacing 5:
                    viewport mousewheel 'change' draggable True id 'vp3':
                        has vbox spacing 5
                        frame xfill True background None:
                            if CurChar == 'max':
                                vbox spacing -1:
                                    for char in sorted(chars.keys()):

                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                $ char_name = chars[char].name_4
                                                text _("Отношения с [char_name!t]:") size 24 color gui.accent_color
                                            frame xfill True background None:
                                                text GetRelMax(char)[1] size 24
                                    frame area (0, 0, 350, 25):
                                        background None

                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Запас сил:") size 24 color gui.accent_color
                                        frame xfill True background None:
                                            text str(round(mgg.energy, 1))+"%" size 24
                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Тренированность:") size 24 color gui.accent_color
                                        frame xfill True background None:
                                            text str(round(mgg.training, 1))+"%" size 24
                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Чистота:") size 24 color gui.accent_color
                                        frame xfill True background None:
                                            text str(round(mgg.cleanness, 1))+"%" size 24

                                    frame area (0, 0, 350, 25):
                                        background None
                                    frame xsize 350 background None:
                                        text _("Cheats") size 26 font 'trebucbd.ttf' color "#bd001f"

                                    hbox xfill True: # Money
                                        frame xsize 300 background None:
                                            text _("Money:") size 24 color "#50c700" yalign 0.5
                                        frame xsize 50 background None:
                                            if mgg._m1_01classes__tange > 100:
                                                imagebutton:
                                                    idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                    hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                    action SetVariable("mgg._m1_01classes__tange", mgg._m1_01classes__tange-100)
                                            else:
                                                text _("")
                                        frame xsize 100 background None:
                                            text str(mgg._m1_01classes__tange) size 24 ycenter 0.4
                                        frame xfill True background None:
                                            imagebutton:
                                                idle im.Scale("images/interface/next_idle.webp",50,25)
                                                hover im.Scale("images/interface/next_hover.webp",50,25)
                                                action SetVariable("mgg._m1_01classes__tange", mgg._m1_01classes__tange+100)

                                    hbox xfill True: # Energy
                                        frame xsize 300 background None:
                                            text _("Energy:") size 24 color "#50c700" yalign 0.5
                                        frame xsize 50 background None:
                                            if mgg.energy > 30:
                                                imagebutton:
                                                    idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                    hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                    action SetVariable("mgg.energy", mgg.energy-10)
                                            else:
                                                text _("")
                                        frame xsize 100 background None:
                                            text str(round(mgg.energy, 1))+"%" size 24 ycenter 0.4
                                        frame xfill True background None:
                                            if mgg.energy < 90:
                                                imagebutton:
                                                    idle im.Scale("images/interface/next_idle.webp",50,25)
                                                    hover im.Scale("images/interface/next_hover.webp",50,25)
                                                    action SetVariable("mgg.energy", mgg.energy+10)
                                            else:
                                                text _("")

                                    hbox xfill True: # Strength
                                        frame xsize 300 background None:
                                            text _("Exercise:") size 24 color "#50c700" yalign 0.5
                                        frame xsize 50 background None:
                                            if mgg.training > 4:
                                                imagebutton:
                                                    idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                    hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                    action SetVariable("mgg.training", mgg.training-1)
                                            else:
                                                text _("")
                                        frame xsize 100 background None:
                                            text str(round(mgg.training, 1))+"%" size 24 ycenter 0.4
                                        frame xfill True background None:
                                            if mgg.training < 99:
                                                imagebutton:
                                                    idle im.Scale("images/interface/next_idle.webp",50,25)
                                                    hover im.Scale("images/interface/next_hover.webp",50,25)
                                                    action SetVariable("mgg.training", mgg.training+1)
                                            else:
                                                text _("")

                                    if mgg.social > 0.1: # Persuasion
                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Persuasion skill:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if mgg.social > 10:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action SetVariable("mgg.social", mgg.social-1)
                                                else:
                                                    text _("")
                                            frame xsize 100 background None:
                                                text str(round(mgg.social*10, 1)) size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if mgg.social < 95:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action SetVariable("mgg.social", mgg.social+1)
                                                else:
                                                    text _("")

                                    if mgg.stealth > 0.1: # Ninja
                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Way of the ninja:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if mgg.stealth > 10:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action SetVariable("mgg.stealth", mgg.stealth-1)
                                                else:
                                                    text _("")
                                            frame xsize 100 background None:
                                                text str(round(mgg.stealth*10, 1)) size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if mgg.stealth < 95:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action SetVariable("mgg.stealth", mgg.stealth+1)
                                                else:
                                                    text _("")

                                    if mgg.massage > 0.1: # Massage
                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Massage skill:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if mgg.massage > 10:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action SetVariable("mgg.massage", mgg.massage-1)
                                                else:
                                                    text _("")
                                            frame xsize 100 background None:
                                                text str(round(mgg.massage*10, 1)) size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if mgg.massage < 95:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action SetVariable("mgg.massage", mgg.massage+1)
                                                else:
                                                    text _("")

                                    if mgg.ero_massage > 0.1: # Ero massage
                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Ero massage skill:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if mgg.ero_massage > 10:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action SetVariable("mgg.ero_massage", mgg.ero_massage-1)
                                                else:
                                                    text _("")
                                            frame xsize 100 background None:
                                                text str(round(mgg.ero_massage*10, 1)) size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if mgg.ero_massage < 95:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action SetVariable("mgg.ero_massage", mgg.ero_massage+1)
                                                else:
                                                    text _("")

                                    if mgg.kissing > 0.1: # Kissing
                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Kissing skill:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if mgg.kissing > 10:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action SetVariable("mgg.kissing", mgg.kissing-1)
                                                else:
                                                    text _("")
                                            frame xsize 100 background None:
                                                text str(round(mgg.kissing*10, 1)) size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if mgg.kissing < 95:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action SetVariable("mgg.kissing", mgg.kissing+1)
                                                else:
                                                    text _("")

                                    if mgg.sex > 0.1: # Sexual experience
                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Sex skill:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if mgg.sex > 10:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action SetVariable("mgg.sex", mgg.sex-1)
                                                else:
                                                    text _("")
                                            frame xsize 100 background None:
                                                text str(round(mgg.sex*10, 1)) size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if mgg.sex < 95:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action SetVariable("mgg.sex", mgg.sex+1)
                                                else:
                                                    text _("")

                                    if mgg.cuni > 0.1: # cuni experience
                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Cunnilingus:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if mgg.cuni > 10:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action SetVariable("mgg.cuni", mgg.cuni-1)
                                                else:
                                                    text _("")
                                            frame xsize 100 background None:
                                                text str(round(mgg.cuni*10, 1)) size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if mgg.cuni < 95:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action SetVariable("mgg.cuni", mgg.cuni+1)
                                                else:
                                                    text _("")

                                    if mgg.anal > 0.1: # Anal experience
                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Anal:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if mgg.anal > 10:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action SetVariable("mgg.anal", mgg.anal-1)
                                                else:
                                                    text _("")
                                            frame xsize 100 background None:
                                                text str(round(mgg.anal*10, 1)) size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if mgg.anal < 95:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action SetVariable("mgg.anal", mgg.anal+1)
                                                else:
                                                    text _("")

                                    frame area (0, 0, 350, 25):
                                        background None
                                    frame xsize 350 background None:
                                        text _("Навыки:") size 26 font 'trebucbd.ttf'
                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Навык убеждения:") size 24 color gui.accent_color
                                        frame xfill True background None:
                                            text str(round(mgg.social*10, 1)) size 24
                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Навык скрытности:") size 24 color gui.accent_color
                                        frame xfill True background None:
                                            text str(round(mgg.stealth*10, 1)) size 24
                                    if mgg.massage > 0:
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Навык массажа:") size 24 color gui.accent_color
                                            frame xfill True background None:
                                                text str(round(mgg.massage*10, 1)) size 24
                                    if mgg.ero_massage > 0:
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Навык эро.массажа:") size 24 color gui.accent_color
                                            frame xfill True background None:
                                                text str(round(mgg.ero_massage*10, 1)) size 24
                                    if mgg.kissing > 0:
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Навык поцелуев:") size 24 color gui.accent_color
                                            frame xfill True background None:
                                                text str(round(mgg.kissing*10, 1)) size 24
                                    if mgg.sex > 0:
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Сексуальный опыт:") size 24 color gui.accent_color
                                            frame xfill True background None:
                                                text str(round(mgg.sex*10, 1)) size 24

                            elif CurChar == 'eric':
                                frame xfill True ysize 15 background None

                            else:
                                vbox spacing -1:

                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Настроение:") size 24 color gui.accent_color
                                        frame xfill True background None:
                                            text chars[CurChar].GetMood()[1] size 24

                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Уровень отношений:") size 24 color gui.accent_color
                                        frame xfill True background None:
                                            text GetRelMax(CurChar)[1] size 24

                                    if chars[CurChar] in infl:
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Влияние Макса:") size 24 color gui.accent_color
                                            frame xfill True background None:
                                                text str(infl[chars[CurChar]].balance[0])+"%" size 24
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Влияние Эрика:") size 24 color gui.accent_color
                                            frame xfill True background None:
                                                text str(infl[chars[CurChar]].balance[1])+"%" size 24

                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Cheats") size 26 font 'trebucbd.ttf' color "#bd001f"

                                    hbox xfill True: # Mood cheat
                                        frame xsize 300 background None:
                                            text _("Mood:") size 24 color "#50c700" yalign 0.5
                                        frame xsize 50 background None:
                                            if chars[CurChar].mood >= -265:
                                                imagebutton:
                                                    idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                    hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                    action Function(change_mood,CurChar,-20)
                                            else:
                                                text _("")
                                        frame xsize 50 background None:
                                            text str(chars[CurChar].mood) size 24 ycenter 0.4
                                        frame xfill True background None:
                                            if chars[CurChar].mood <= 480:
                                                imagebutton:
                                                    idle im.Scale("images/interface/next_idle.webp",50,25)
                                                    hover im.Scale("images/interface/next_hover.webp",50,25)
                                                    action Function(change_mood,CurChar,20)
                                            else:
                                                text _("")

                                    hbox xfill True: # Relationship cheat
                                        frame xsize 300 background None:
                                            text _("Relationship with Max:") size 24 color "#50c700" yalign 0.5
                                        frame xsize 50 background None:
                                            if chars[CurChar].relmax >= -350:
                                                imagebutton:
                                                    idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                    hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                    action Function(change_relationship,CurChar,-50)
                                            else:
                                                text _("")
                                        frame xsize 50 background None:
                                            text str(chars[CurChar].relmax) size 24 ycenter 0.4
                                        frame xfill True background None:
                                            if chars[CurChar].relmax <= 1550:
                                                imagebutton:
                                                    idle im.Scale("images/interface/next_idle.webp",50,25)
                                                    hover im.Scale("images/interface/next_hover.webp",50,25)
                                                    action Function(change_relationship,CurChar,50)
                                            else:
                                                text _("")

                                    if (chars[CurChar] in infl) and (not infl[chars[CurChar]].freeze) and (flags.eric_banished < 1) and (infl[chars[CurChar]]._m1_01classes__m is not None): # influence cheat
                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Max's influence:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if (infl[chars[CurChar]]._m1_01classes__m  >= 10):
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action Function(change_influence,CurChar,-10)
                                                else:
                                                    text _("")
                                            frame xsize 50 background None:
                                                text str(infl[chars[CurChar]].balance[0])+"%" size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if (infl[chars[CurChar]]._m1_01classes__m  <= 190):
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action Function(change_influence,CurChar,10)
                                                else:
                                                    text _("")

                                        hbox xfill True:
                                            frame xsize 300 background None:
                                                text _("Eric's influence:") size 24 color "#50c700" yalign 0.5
                                            frame xsize 50 background None:
                                                if (infl[chars[CurChar]]._m1_01classes__e  >= 10):
                                                    imagebutton:
                                                        idle im.Scale("images/interface/prev_idle.webp",50,25)
                                                        hover im.Scale("images/interface/prev_hover.webp",50,25)
                                                        action Function(change_influence,CurChar,10)
                                                else:
                                                    text _("")
                                            frame xsize 50 background None:
                                                text str(infl[chars[CurChar]].balance[1])+"%" size 24 ycenter 0.4
                                            frame xfill True background None:
                                                if (infl[chars[CurChar]]._m1_01classes__e  <= 190):
                                                    imagebutton:
                                                        idle im.Scale("images/interface/next_idle.webp",50,25)
                                                        hover im.Scale("images/interface/next_hover.webp",50,25)
                                                        action Function(change_influence,CurChar,-10)
                                                else:
                                                    text _("")
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Influence holder:") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                if infl[chars[CurChar]].balance[2] == 'm':
                                                    text _("Max") size 24 ycenter 0.4
                                                elif infl[chars[CurChar]].balance[2] == 'e':
                                                    text _("Eric") size 24 ycenter 0.4
                                                elif infl[chars[CurChar]].balance[1] == infl[chars[CurChar]].balance[0]:
                                                    text _("There can be only one") size 24 ycenter 0.4
                                                else:
                                                    text _("What the fuck happened??") size 24 ycenter 0.4

                                    if CurChar == 'alice': # Alice specific cheats
                                        if poss['smoke'].st () > 2 and punalice[0][1] == 0 and tm < '18:00' and 0 < weekday < 6: # Punish Alice
                                            hbox xfill True:
                                                frame xsize 150 background None:
                                                    text _("Punish Alice") size 24 color "#50c700" yalign 0.5
                                                frame xfill True background None:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/touch.webp",40,25)
                                                        action Function (punish_alice)
                                    
                                        hbox xfill True: # Stats
                                            frame xsize 350 background None:
                                                text _("Stats") size 26 font 'trebucbd.ttf' color "#bd001f"
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Total punishments") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                text str(alice.flags.pun) size 24 ycenter 0.4
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Total times protected") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                text str(alice.flags.defend) size 24 ycenter 0.4
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Times protected this week") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                text str(alice.weekly.protected) size 24 ycenter 0.4
                                                                        
                                    if CurChar == 'lisa': # Lisa specific cheats
                                        if poss['sg'].st() > 2 and punlisa[1][0] == 0 and tm < '18:00' and 0 < weekday < 6: # Punish Lisa
                                            hbox xfill True:
                                                frame xsize 150 background None:
                                                    text _("Punish Lisa") size 24 color "#50c700" yalign 0.5
                                                frame xfill True background None:
                                                    imagebutton:
                                                        idle im.Scale("images/interface/touch.webp",40,25)
                                                        action Function (punish_lisa)
                                    
                                        hbox xfill True: # Stats
                                            frame xsize 350 background None:
                                                text _("Stats") size 26 font 'trebucbd.ttf' color "#bd001f"
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Homework help this week") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                text str(lisa.weekly.help) size 24 ycenter 0.4
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Hand massage this week") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                text str(lisa.weekly.mass1) size 24 ycenter 0.4
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Help with dishes this week") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                text str(lisa.weekly.dishes) size 24 ycenter 0.4
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Times protected this week") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                text str(lisa.weekly.protected) size 24 ycenter 0.4
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Total times punished") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                text str(lisa.flags.pun) size 24 ycenter 0.4
                                        hbox xfill True:
                                            frame xsize 350 background None:
                                                text _("Total times protected") size 24 color "#50c700" yalign 0.5
                                            frame xfill True background None:
                                                text str(lisa.flags.defend) size 24 ycenter 0.4

                        frame xfill True background None:
                            has vbox spacing 5
                            if CurChar == 'lisa':
                                if lisa.dcv.shower.stage == 1:

                                    text _("Лучше пока не попадаться на подглядывании за Лизой в душе")
                                if len(lisa.sorry.give):
                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Предпочтения в сладостях:") size 24 color gui.accent_color
                                        frame xfill True background None:
                                            has vbox spacing 1
                                            if 3 in lisa.sorry.give:
                                                text _("Любит \"Ritter Sport\"") size 24
                                            if 2 in lisa.sorry.give:
                                                text _("Сгодится \"Raffaello\"") size 24
                                            if 1 in lisa.sorry.give:
                                                text _("Ненавидит \"Ferrero Rocher\"") size 24


                                if poss['sg'].used(10):
                                    frame xsize 350 background None:
                                        text _("Предпочтения в массаже:") size 24 color gui.accent_color
                                    frame xpos 20 xsize 790 background None:
                                        has vbox spacing 10
                                        text _("- После массажа рук Лиза может позволить массировать ей плечи (и не только их) при выполнении домашнего задания") size 24 justify True
                            elif CurChar == 'alice':
                                if alice.dcv.shower.stage == 1:

                                    text _("Лучше пока не попадаться на подглядывании за Алисой в душе")
                                if len(alice.sorry.give):
                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Предпочтения в сладостях:") size 24 color gui.accent_color
                                        frame xfill True background None:
                                            has vbox spacing 1
                                            if 3 in alice.sorry.give:
                                                text _("Любит \"Ferrero Rocher\"") size 24
                                            if 2 in alice.sorry.give:
                                                text _("Сгодится \"Ritter Sport\"") size 24
                                            if 1 in alice.sorry.give:
                                                text _("Ненавидит \"Raffaello\"") size 24
                                if poss['nightclub'].used(5):
                                    hbox xfill True:
                                        frame xsize 350 background None:
                                            text _("Действие алкоголя:") size 24 color gui.accent_color
                                        if alice.flags.incident<1:
                                            frame xfill True background None:
                                                text _("???") size 24
                                if alice.flags.incident in [2, 4]:
                                    frame xpos 20 xsize 790 background None:
                                        has vbox spacing 10
                                        text _("- Не может вспомнить всё, что происходило, пока она была пьяна") size 24 justify True first_indent -20
                                if learned_foot_massage():
                                    frame xsize 350 background None:
                                        text _("Предпочтения в массаже:") size 24 color gui.accent_color
                                    frame xpos 20 xsize 790 background None:
                                        has vbox spacing 10
                                        text _("- Если начинать массаж для Алисы во дворе со ступней, то вероятность помассировать остальное больше") size 24 first_indent -20
                                        if alice.stat.footjob:
                                            text _("- При помощи конфет с ликёром можно получить фут-джоб (и не только) от Алисы при массаже у ТВ") size 24 first_indent -20
                                        if alice.flags.hip_mass:
                                            text _("- Получив фут-джоб от Алисы при массаже у ТВ, есть шанс увидеть через камеру, как она мастурбирует перед сном") size 24 first_indent -20

                            frame xfill True ysize 15 background None

                    vbar value YScrollValue('vp3') style 'info_vscroll'

        key 'K_ESCAPE' action Jump('AfterWaiting')
        key 'mouseup_3' action Jump('AfterWaiting')

init python:
    def change_mood(char_name, amount):
        chars[char_name].mood += amount

    def change_relationship(char_name, amount):
        chars[char_name].relmax += amount

    def change_influence(char_name,amount):
        if amount >= 0:
            infl[chars[char_name]].add_m(amount)
            if (infl[chars[char_name]]._m1_01classes__e < amount):
                pass
            else:
                infl[chars[char_name]].sub_e(amount)
        else:
            infl[chars[char_name]].add_e(abs(amount))
            if (infl[chars[char_name]]._m1_01classes__m < amount):
                pass
            else:
                infl[chars[char_name]].sub_m(abs(amount))

    def australian_mode():
        poss['spider'].open(2)
        items['spider'].have = True

    def punish_alice():
        if alice.dcv.special.done:
            punalice[0][1] = 1
        else:
            alice.dcv.special.done = True
            punalice[0][1] = 1

    def punish_lisa():
        punlisa[1][0] = 1