define bd = Character("Brent Dackris", color = "#594896") #Main Character
define gf = Character("Guia Franian", color = "#f12f6d") #BFF
define kd = Character("Karen Danilo", color = "#a3a800") #Student 1
define s1sil = Character("???", color = "#a3a800") #kd
define s2sil = Character("???", color = "#eb5e01") #mg
define mg = Character("Marc Gregorio", color = "#eb5e00") #Student 2
define cn = Character("Chester Nindsey",color = "#286ffc") #Concerned student


label start: #introduction
    scene bg schoolcampus with dissolve:
        zoom 0.9 ypos -150

    play music "audio/hallway.ogg" fadein 1.0
    
    "Today is the first day of school at Mendo Private College..."

    scene bg announce with dissolve:
        zoom 1.5

    pause

    show bd masayaopen at left with moveinleft:
        size(500, 646)

    #pause

    bd "Good morning everyone! Today is..."

    hide bd with dissolve

    show kd shocked at left with moveinleft:
        size(500, 646) yalign 2.0

    s1sil "You see that hottie on the stage?"

    hide kd with dissolve

    show mg normal1 at left with moveinleft:
        size(500, 646)

    s2sil "Yeah. He is Brent Dackris, right? The president of this year's Student Council?"

    hide mg with dissolve

    show kd shocked at left with dissolve:
        size(500, 646) yalign 2.0

    s1sil "OMG! He's so cute and hot! He looks like an intelligent person that gives off strong aura!"

    hide kd with dissolve

    show bd masayaclose at left with dissolve:
        size(500, 646)

    bd "Once again, on behalf of the student council, I welcome you to our beloved college. May we have a fruitful and wonderful year! Thank you!"

#PART NI DANN (page 2)
label body:
    scene bg hall with dissolve:
        xpos -250 zoom 0.8
    "After the opening ceremony, Brent walks with his best friend, Guia Franian, who is the Student Council Vice-President."

    show bd masayaopen at left with moveinleft:
        size(500, 646) 

    # show ig post:
    #     zoom 0.1 xpos 0.50 ypos 0.30

    bd "First day of school really excites me! Look at this photo Guia! I’m so hot here! This is instagramable, right?"

    "Brent showed Guia his photo with two students accidentally showing in the background which may get them bashed."

    window hide

    show ig post with dissolve:
        zoom 0.7 xalign 0.5 yalign 0.5

    pause

    hide ig post with dissolve

    hide bd with dissolve

    show gf a at left with moveinleft:
        size(500, 646)
    
    menu:
        "What should Guia Franian say?"

        "Yeah right. But look, Karen and Marc are caught chatting here, you still want to post it?":
            jump choice2A        
                
        "No! Haha, you look like those ugly bastards in the back":
            jump choice2B           
    
label choice2A:

    #hide ig post

    show gf a at left:
        size(500, 646)

    gf "Yeah right. But look, Karen and Marc are caught chatting here, you still want to post it?" 

    hide gf with dissolve

    show bd smirk at left with dissolve:
        size(500, 646)
#
    bd "Of course, who cares about them? After all, people will only look at me, not those ugly bastards."
        
    "However, Brent seems to be a narcissist. He is also an active social-media user, who tends to be unaware of his actions and limits as a netizen."

    hide bd with dissolve
        
    show gf c at left with dissolve:
        size(500, 646) xpos -50

    gf "Sheesh! Just post whatever you want. But yeah, you look good in there."

    hide gf with dissolve

    show bd masayaopen at left with dissolve:
        size(500, 646)

    bd "Right? I’m sure this will get tons of likes and comments!"

    hide bd with moveoutleft

    "Brent posted the picture. As expected, he received lots of reactions. However many people bashed the photo bombers saying they only ruined the said picture."
        
    jump rising_action
        
    
label choice2B:
    show gf b at left with dissolve:
        size(500, 646) xpos -50

    gf "No! Haha, you look like those ugly bastards in the back."

    hide gf with dissolve

    show bd shocked at left with dissolve:
        size(500, 646) xpos -90

    bd "Wow! But I'm not so ugly like you!"

    hide bd with dissolve

    show gf d at left with dissolve:
        size(500, 646) xpos -50

    gf "Woah, chill. I'm just joking bruh, you do look good in the photo–"

    hide gf with dissolve

    show bd complain at left with dissolve:
        size(500, 646) xpos -50

    bd "I don’t want to be friends with you anymore, you hurt my feelings."

    scene bg black with dissolve

    "You will now be returned to the last checkpoint."

    jump body
    
label rising_action:
    scene bg schoolbackyard3 with dissolve:
        ypos -300

    "The next day..."

    show mg worried at left with moveinleft:
        size(500, 646) xpos -30 yalign 1.2

    mg "Karen, have you seen Brent's post on Instagram?" 

    hide mg with dissolve

    show kd himarc at left with moveinleft:
        size(500, 646) xpos -50 yalign 2.0

    kd "Oh, Hi Marc! Nope, Why? What is it all about?"

    hide kd with dissolve

    "Marc showed Guia the Instagram post with them in the background which Brent posted the other day."

    show ig post with dissolve:
        zoom 0.7 xalign 0.5 yalign 0.5

    window hide
    pause
    hide ig post with dissolve

    show ig cropped with dissolve:
        yalign 0.5 xalign 0.5 zoom 1.1

    pause
    
    hide ig cropped with dissolve
    #hide ig post

    show kd shocked at left with dissolve:
        size(500, 646) xpos -80 yalign 2.0

    kd "OMG! How could he have done this to you, to me, to all of us!!? I am so dissapointed in him!"

    hide kd with dissolve

    show mg saddissapointedhehe at left with dissolve:
        size(500, 646) yalign 2.5

    mg "He could've thought about it twice before posting. Now, many people are bashing us even though we did nothing wrong!"

    scene bg schoolbackyard2 with dissolve:
        ypos -300

    "With mixed feelings of anger and distress, Karen and Marc approaches Brent."

    "Karen and Marc confronts Brent."

    show mg normal1 at left with moveinleft:
        size(500, 646) xpos -50

    mg "Brent, we need to talk."

    hide mg with dissolve

    show bd nagccp at left with moveinleft:
        size(500, 646) yalign 1.2

    pause

    hide bd with dissolve

    show mg normal2 at left with dissolve:
        size(500, 646) xpos -50

    mg "Brent! We have something important to say."

    hide mg with dissolve

    show bd normal at left with dissolve:
        size(500, 646) xpos -70

    bd "..."

    hide bd with dissolve
    
    show kd grabphone at left with moveinleft:
        size(500, 646) xpos -100 yalign 1.2

    with hpunch

    "Karen grabs the phone and slaps Brent's face."

    hide kd with dissolve

    show bd shocked at left with dissolve:
        size(500, 646) xpos -100

    bd "What the frick?! What's your problem bruh?"

    hide bd with dissolve

    show kd shw at left with dissolve:
        size(500, 646) xpos -80 yalign 1.2

    kd "Look what you've done!"

    show ig post with dissolve

    pause

    hide ig post with dissolve

    show kd angry at left with dissolve:
        size(500, 646) xpos -80 yalign 1.2

    kd "Because of that picture where you think you're that good-looking, we got bashed!"

    hide kd with dissolve

    show bd normal at left with dissolve:
        size(500, 646)

    menu: #choice 2
        "What should Brent say?"

        "Well, I don't care about that! It's not my business anymore!":
            jump choice2a

        "Woahhh, really? I'm really sorry for that.":
            jump choice2b

label choice2a:
    show bd rolledeyes at left with dissolve:
        size(500, 646) xpos -80 yalign 1.2

    bd "Well, I don't care about that! It's not my business anymore!"
    
    jump choice2cont

label choice2b:
    show bd normal at left with dissolve:
        size(500, 646)

    bd "Woah, really? I'm really sorry for that."

    show bd rolledeyes at left with dissolve:
        size(500, 646)

    bd "But I really think it's not my business anymore!"
    
    jump choice2cont

label choice2cont:
    hide bd with dissolve

    show mg shockedangry at left with dissolve:
        size(500, 646) xpos -50 yalign 1.2

    mg "You don't care about that?? You just made a hundred people bad-mouth and laugh at us!"

    hide mg with dissolve

    show bd angry at left with dissolve:
        size(500, 646) xpos -80

    bd "It's not my fault that you guys are ugly!"

    show bd rolledeyes at left with dissolve:
        size(500, 646) xpos -80 yalign 1.2

    bd "Duh! I'm an influencer who has a lot of followers."

    hide bd with dissolve

    show mg nakanganga1 at left with dissolve:
        size(500, 646) xpos -80 yalign 1.2

    mg "Why don't you just say that you're sorry? Is that even hard to say?"

    hide mg with dissolve

    show kd worried at left with dissolve:
        size(500, 646) xpos -100

    kd "You posted a picture of us without our consent. You must delete it now before something bad happens."

    hide kd with dissolve

    show bd rolledeyes with dissolve:
        size(500, 646) xpos -80 yalign 1.2

    menu: #choice3:
        "What should Brent Dackris say?"

        "Why should I? You're just no one.":
            jump choice3a

        "Okay, fine. I'm sorry. Happy now?":
            jump choice3b

label choice3a:
    show bd smirk at left with dissolve:
        size(500, 646)

    bd "Why should I? You're just no one."

    jump climax

label choice3b:
    show bd rolledeyes at left with dissolve:
        size(500, 646) yalign 1.2
    bd "Okay, fine. I'm sorry. Happy now?"

    show bd smirk at left with dissolve:
        size(500, 646)

    bd "*whispers to self* I'm not going to delete it though. Haha, losers."

    jump climax

label climax:
    hide bd with dissolve

    show gf o at left with moveinleft:
        size(500, 646) xpos -90

    gf "Brent! What's happening here?"

    hide gf with dissolve

    show mg nakanganga1 at left with dissolve:
        size(500, 646) xpos -100 yalign 1.2

    mg "Oh! You're the Vice President of the Student Council, right?"

    hide mg with dissolve

    show gf e at left with dissolve:
        size(500, 646) xpos -100

    gf "Yes. So? What's happening here?"

    hide gf with dissolve

    show bd angry at left with dissolve:
        size(500, 646) xpos -80

    bd "These two! They want me to delete my post because many people are bashing them!"

    hide bd with dissolve

    show gf o at left with dissolve:
        size(500, 646) xpos -100 yalign 1.2

    menu: #choice4

        "What should Guia Franian Say?"

        "Yeah, you should delete it, Brent. I saw the bashers' reactions too. It's not good anymore.":
            jump choice4a

        "Well, I mean you two do look ugly in the photo, but Brent you should delete it anyway.":
            jump choice4b

label choice4a:
    show gf o at left with dissolve:
        size(500, 646) xpos -90
    
    gf "Yeah, you should delete it, Brent. I saw the bashers' reactions too. it's not good anymore."

    hide gf with dissolve

    show bd complain at left with dissolve:
        size(500, 646) xpos -100

    bd "What? You too, Guia?"

    jump choice4cont

label choice4b:
    show gf c at left with dissolve:
        size(500, 646) xpos -90
    
    gf "Well, I mean you two do look ugly in the photo, but Brent you should delete it anyway."

    hide gf with dissolve

    show bd complain at left with dissolve:
        size(500, 646) xpos -100

    bd "No way! Why should I?"

    hide bd with dissolve

    show gf o at left with dissolve:
        size(500, 646) xpos -90

    gf "I saw the bashers’ reactions too. It’s not good anymore."
    
    jump choice4cont

label choice4cont:
    hide gf with dissolve

    hide bd with dissolve
    #hide mg

    show kd nakanganga at left with dissolve:
        size(500, 646) xpos -80

    kd "See, President? So please, delete it."

    hide kd with dissolve
    
    show bd disappointed at left with dissolve:
        size(500, 646)

    bd "Guia! No!"

    hide bd with dissolve

    show gf g at left with dissolve:
        size(500, 646) xpos -80

    gf "Brent, just delete it."

    hide gf with dissolve

    show bd angry at left with dissolve:
        size(500, 646) xpos -80

    bd "Fine!"

    hide bd with dissolve

    "Brent deletes the post."
    
    show bd complain at left with dissolve:
        size(500, 646) xpos -50

    bd "Is that okay now?? If it's fine, leave!"

    stop music fadeout 1.0

#dann hanggang student council
label roomniguia:
    play music "audio/room.ogg" fadein 1.0
    scene bg guiasroom with dissolve

    window hide

    pause

    "The night after the confrontation…"

    "In Guia’s room…"

    show gf h at left with moveinleft:
        size(500, 646) xpos -80

    gf "Why and how did Brent turn out like this? He’s not like this before."

    show gf i at left with dissolve:
        size(500, 646) xpos -80

    gf "Day after day, he’s becoming different from the Brent I knew."

    show gf c at left with dissolve:
        size(500, 646) xpos -80

    gf "The Brent who’s soft, a bookworm, awkward, clumsy, and kind has now turned into the..."

    gf "Brent who's an arrogant, narcissistic attention seeker."

    show gf h at left with dissolve:
        size(500, 646) xpos -80

    gf "It’s disappointing."

    show gf i at left with dissolve:
        size(500, 646) xpos -80

    gf "This is just like what he did before. I can still remember the hurtful comments and..."

    gf "reactions when he posted his picture with me, who fell from the stairs, and I can still..."

    gf "remember how he remained ignorant about the situation."

    show gf j at left with dissolve:
        size(500, 646) xpos -80

    gf "This must stop. This time…"

    menu: #choice5
        "This must stop. This time..."
        
        #show serious look
        "Brent needs to learn his lesson.":  
            jump choice5a
        #show evil look
        "Brent needs some punishment.": 
            jump choice5b

label choice5a:
    show gf k at left with dissolve:
        size(500, 646) xpos -80
    gf "Brent needs to learn his lesson." 

    gf "I will hack his account."

    jump StudentCouncilRoom

label choice5b:
    show gf j at left with dissolve:
        size(500, 646) xpos -80

    gf "Brent needs some punishment."

    gf "I will hack his account."

    stop music fadeout 1.0

    jump StudentCouncilRoom

label StudentCouncilRoom:
    scene bg studentcouncilroom with dissolve:
        zoom 0.79 yalign 1.0

    play music "audio/room.ogg" fadein 1.0

    window hide

    pause

    "The next day in the Student Council room…"
    
    show gf f at left with moveinleft:
        size(500, 646) xpos -80

    gf "Hi, Brent! What are you doing?"

    hide gf with dissolve

    show bd nagccp at left with moveinleft:
        size(500, 646) yalign 1.2

    bd "..."

    hide bd with dissolve

    show gf h at left with dissolve:
        size(500, 646) xpos -80

    gf "*Thinks to herself* Hmmm... Social media again huh."

    show gf i at left with dissolve:
        size(500, 646) xpos -80
    
    gf "*Thinks to herself* Did he just... posted a picture with his location written on the caption?"

    show gf h at left with dissolve:
        size(500, 646) xpos -80

    gf "*Thinks to herself* Huh, commenting on others' posts..."

    show gf i at left with dissolve:
        size(500, 646) xpos -80
    
    gf "*Thinks to herself* Oh HE DID NOT just share a controversial post."

    show gf o at left with dissolve:
        size(500, 646) xpos -80

    gf "Brent, you know what? You must limit yourself when using social media."

    hide gf with dissolve

    show bd shocked at left with dissolve:
        size(500, 646) xpos -80

    bd "Oh, Guia. You scared me. Why? I am not doing anything wrong."

    hide bd with dissolve

    show gf c at left with dissolve:
        size(500, 646) xpos -80

    menu: #choice 5.1
        "What should Guia say?"

        "Maybe you should start to know the consequences of what you are doing on social media. You never know.":
            jump choice51a

        "Oh, so you think you’re not doing anything wrong?":
            jump choice51b

label choice51a:
    show gf c at left with dissolve:
        size(500, 646) xpos -80

    gf "Maybe you should start to know the consequences of what you are doing on social media. You never know."

    hide gf with dissolve

    show bd fakesmile at left with dissolve:
        size(500, 646) xpos -80

    bd "Fine. Fine. Anyways, it’s my personal account… so I can do whatever I want."

    jump choice51cont

label choice51b:
    show gf o at left with dissolve:
        size(500, 646) xpos -80

    gf "Oh, so you think you’re not doing anything wrong?"

    hide gf with dissolve

    show bd fakesmile at left with dissolve:
        size(500, 646) xpos -80

    bd "Of course! This is my personal account, and I have the right to do whatever I want! Right? Right?"

    jump choice51cont

label choice51cont:
    hide bd with dissolve

    show gf i at left with dissolve:
        size(500, 646) xpos -80

    gf "Okay... It's up to you. I warned you anyway."

    stop music fadeout 1.0

    play music "audio/hallway.ogg" fadein 1.0

    scene bg hall with dissolve:
        xpos -250 zoom 0.8

    pause

    show gf j at left with moveinleft:
        size(500, 646) xpos -80
    
    gf "He never really learned, guess I should do it after all."

    stop music fadeout 1.0

    jump Hackingtime

label Hackingtime:
    scene bg guiasroom with dissolve

    play music "audio/room.ogg" fadein 1.0

    window hide

    pause
    
    "That night, Guia decided to enact her plan to hack Brent."

    show gf h at left with moveinleft:
        size(500, 646) xpos -50

    gf "Now if I remember correctly, Brent overshared and revealed his password in a subtle, accidental way."

    show gf k at left with dissolve:
        size(500, 646) xpos -50

    gf "I knew it! It was when Brent left his laptop open while his username and password are displayed!"
    gf "I know I noted it..."

    scene bg hack with dissolve:
        zoom 0.8

    pause

    show gf h at left with moveinleft:
        size(500, 646) xpos -50

    gf "Ah! found it."

    ##### DECIDE IF MAGLALAGAY PA NG NOTE

    menu: #choice 6
        "Do it.":
            jump choice6cont

        "Don't do it.":
            jump choice6b

label choice6b:
    #hide note unpw

    #show guia determined

    gf "No, I must do this for the sake of Brent."

    menu:
        "Do it.":
            jump choice6cont

label choice6cont:
    scene bg login with dissolve:
        xalign 0.4 yalign 0.3

    pause

    show gf k at left with moveinleft:
        size(500, 646) xpos -80

    gf "Alright, here we go."

    show gf f at left with dissolve:
        size(500, 646) xpos -80

    play sound "audio/type.ogg" fadein 1.0
    
    gf "Hehe. Imagine having 'brent123' as a password."

    scene bg guiasroom with dissolve

    show gf i at left with moveinleft:
        size(500, 646) xpos -80

    gf "Now let's post these as a harmless prank to teach him a lesson."

    #hide gf

    show ig raw1 with dissolve:
        zoom 0.5 xalign 0.7 yalign 0.5

    pause

    hide ig raw1 with dissolve

    show ig raw2 with dissolve:
        zoom 0.5 xalign 0.7 yalign 0.5

    pause

    hide ig raw2 with dissolve

    stop sound fadeout 1.0

    show gf f at left with dissolve:
        size(500, 646) xpos -80

    gf "That should do it."

    stop music fadeout 1.0

    scene bg cafeteria2 with dissolve

    play music "audio/hallway.ogg" fadein 1.0

    window hide

    pause

    "The next day, Brent is walking alone in the school canteen. After some time, someone approaches him."

    #show bd normal at left

    show cn happy at left with moveinleft:
        size(500, 646) xpos -70

    cn "Hey! President! I'm just curious, why did you post those things on Instagram last night?"

    hide cn with dissolve

    show bd confused at left with moveinleft:
        size(500, 646) xpos -80

    menu: #choice7
        "What should Brent say?"

        "Huh? What do you mean?":
            jump choice7a

        "Last night?? Or do you mean my picture that gained more than a thousand reactions from two days ago?":
            jump choice7b

label choice7a:
    show bd confused at left with dissolve:
        size(500, 646) xpos -80
    
    bd "Huh? What do you mean?"

    hide bd with dissolve

    show cn o at left with dissolve:
        size(500, 646) yalign 1.2 xpos -70

    cn "Last night, you were active on Instagram and I've seen you posting about your not-so-good-looking pictures, as well as infos about hackers and netiquettes."

    hide cn with dissolve
    
    jump choice7cont

label choice7b:
    show bd confused at left with dissolve:
        size(500, 646) xpos -80

    bd "Last night?? Or do you mean my picture that gained more than a thousand reactions from two days ago?"

    jump choice7cont

label choice7cont:
    show bd confused at left with dissolve:
        size(500, 646) xpos -80

    bd "What do you mean about posts about hackers and stuff?"

    hide bd with dissolve

    show cn o at left with dissolve:
        size(500, 646) yalign 1.2
    
    cn "Huh? I mean, look at this…"

    hide cn with dissolve

    show ig hackeda with dissolve:
        zoom 0.4 xalign 0.5 yalign 0.5

    pause

    hide ig hackeda with dissolve
    
    show ig hacked1 with dissolve:
        zoom 0.4 xalign 0.5 yalign 0.5

    pause

    hide hacked1 with dissolve

    show ig hacked2 with dissolve:
        zoom 0.4 xalign 0.5 yalign 0.5

    pause

    hide ig hacked2 with dissolve

    show ig hackedc with dissolve:
        zoom 0.4 xalign 0.5 yalign 0.5

    pause

    hide ig hackedc with dissolve

    show ig hackedd with dissolve:
        zoom 0.4 xalign 0.5 yalign 0.5

    pause

    hide ig hackedd with dissolve

    show ig hackede with dissolve:
        zoom 0.4 xalign 0.5 yalign 0.5

    pause

    hide ig hackede with dissolve

    show ig hackedf with dissolve:
        zoom 0.4 xalign 0.5 yalign 0.5

    pause

    hide ig hackedf with dissolve

    show bd shocked at left with dissolve:
        size(500, 646) xpos -80

    bd "What the frick is this? Sheesh!"

    show bd denial at left with dissolve:
        size(500, 646) xpos -80
    
    bd "I didn’t post this!"

    show bd angry at left with dissolve:
        size(500, 646) xpos -80
    
    bd "So, how come it’s in my feed?"
    
    hide bd with dissolve

    show cn shocked at left with dissolve:
        size(500, 646)

    #show cn surprised

    cn "I knew something was strange about it. Why don’t you check it out yourself? It looks like your account was hacked!"

    hide cn with dissolve

    show bd complain at left with dissolve:
        size(500, 646)

    menu: #choice8
        "what should Brent say?"

        "No way! This can’t happen! I’ve done nothing wrong on my account.":
            jump choice8a

        "You’re joking right? This is not funny. You can be reported based on your actions.":
            jump choice8b

label choice8a:
    show bd complain at left:
        size(500, 646)
    bd "No way! This can’t happen! I’ve done nothing wrong with my account."

    hide bd with dissolve
    
    show cn straight at left with dissolve:
        size(500, 646)
    cn "Yes, you probably didn’t do anything. But given your actions, someone really hacked your account."

    jump choice8cont

label choice8b:
    show bd complain at left with dissolve:
        size(500, 646)

    bd "You’re joking right? This is not funny. You can be reported based on your actions."
    
    hide bd with dissolve

    show cn straight at left with dissolve:
        size(500, 646)

    cn "What? Do you think I’m joking? I’m just concerned about this. You should be thankful I updated you about it, otherwise you’d be the talk-of-the-town."
    
    jump choice8cont
    
label choice8cont:
    cn "Also, you know what? In your past posts, I observed that you have been posting whatever you like regardless of whether anyone gets hurt."   

    hide cn with dissolve

    show bd angry at left with dissolve:
        size(500, 646)

    bd "Bruh, what are you talking about?"

    hide bd with dissolve

    show cn happyface2 at left with dissolve:
        size(500, 646) yalign 1.2 xpos -70

    #show cn alternating x o

    cn "I’m sorry if this is too much for you, but I think you must know your limits when posting on social media."

    show cn happy at left with dissolve:
        size(500, 646) xpos -70
    
    cn "I get it that you're famous enough to gain such reactions, but there were times that other people got hurt and they were just reacting out of such poor display which is your behavior."

    show cn o at left with dissolve:
        size(500, 646) yalign 1.2 xpos -70
    
    cn "You are smart, famous, hot, and everything, but I don’t think that you would expose too much of yourself on social media. Those are the reasons why I think this happened to you."

    show cn happy at left with dissolve:
        size(500, 646) xpos -70

    cn "I am not happy nor sad about this incident, but in my opinion, you must reflect on your actions. I just hope that in that process, you can recover your account and find the hacker."

    hide cn with dissolve

    show bd denial at left with dissolve:
        size(500, 646)

    bd "I have done nothing wrong!"

    hide bd with dissolve

    show cn o at left with dissolve:
        size(500, 646) yalign 1.2 xpos -70

    cn "You can reflect on that."

    stop music fadeout 1.0

    jump confrontation

#page 8
label confrontation:
    scene bg studentcouncilroom with dissolve:
        zoom 0.79 yalign 1.0

    play music "audio/room.ogg" fadein 1.0

    pause
    show bd complain at left with moveinleft:
        size(500, 646)
    bd "Guia, are you here? Did you know what happened to my account last night?"

    hide bd with dissolve
    
    show gf l at left with moveinleft:
        size(500, 646) xpos -80

    gf "Hey Brent! No, why? What happened to your account?"

    hide gf with dissolve

    show bd complain at left with dissolve:
        size(500, 646)

    bd "It was hacked. I don't know who, why or how, but it was hacked."

    hide bd with dissolve
    
    show gf o at left with dissolve:
        size(500, 646) xpos -80

    menu: #choice9
        "Guia's response is..."
        
        "Really? So the rumors are true!":
            jump choicepage9a
        "Oh, I'm sorry about that, but yeah...I've been hearing a lot about that outside.":
            jump choicepage9b

label choicepage9a:
    show gf o at left with dissolve:
        size(500, 646) xpos -80

    gf "Really? So the rumors are true!"

    hide gf with dissolve
    
    show bd angry at left with dissolve:
        size(500, 646)
    
    bd "Rumors? So you already know about it and you didn’t care to tell me?! What kind of friend are you?!"
    
    jump confrontation_continuation

label choicepage9b:
    show gf o at left with dissolve:
        size(500, 646) xpos -80

    gf "Oh, I'm sorry about that, but yeah...I've been hearing a lot about that outside."

    show bd angry at left with dissolve:
        size(500, 646) xpos -80
    
    bd "Rumors? So you already know about it and you didn’t care to tell me?! What kind of friend are you?!"

    hide gf with dissolve
    
    show bd sad at left with dissolve:
        size(500, 646)

    bd "So everyone was already aware of it? Damn it, I feel embarrassed."

    jump confrontation_continuation

label confrontation_continuation:
    show bd sad at left with dissolve:
        size(500, 646)

    bd "Why are they doing these to me? I didn't do anything wrong! Tell me Guia, what will I do? I can't access my account anymore."
    
    hide bd with dissolve

    show gf x at left with dissolve:
        size(500, 646) xpos -80
    
    gf "Just calm down. First of all, why do you think they did this to you?"

    hide gf with dissolve
    
    show bd sad at left with dissolve:
        size(500, 646)
    
    bd "Honestly, I don't know, but coming into realization, I think Chester is correct."
    
    bd "It's my fault why this happened. I didn't limit myself when using social media."

    show bd normal at left with dissolve:
        size(500, 646)
    
    bd "I was careless and impulsive. And maybe the hacker knows how fragile I am and my account."
    
    bd "The hacker might also be someone I hurt because of my posts. I feel so bad about myself, Guia. I admit, this is all my fault, but I hope they will still return my account."

    stop music fadeout 1.0
    
    jump Guia_Room

label Guia_Room:
    scene bg guiasroom with dissolve

    play music "audio/room.ogg" fadein 1.0

    window hide
    
    pause
    
    "That night in Guia's room..."

    show gf x at left with moveinleft:
        size(500, 646) xpos -80
    
    gf "I never thought the famous Brent Dackris would contemplate his actions that quickly!"
    
    gf "But I guess he was so serious about it." 

    show gf f at left with dissolve:
        size(500, 646) xpos -80
    
    gf "Also, I feel so bad doing this to him. I just love him so much that I don't want him to suffer anymore."
    
    gf "Guess, I'll be giving back his account now."

    stop music fadeout 1.0
    
    jump School

label School:
    scene bg schoolcampus with dissolve:
        zoom 0.9 ypos -150
    
    play music "audio/hallway.ogg" fadein 1.0

    pause

    "The next day..."

    show bd masayaopen at left with moveinleft:
        size(500, 646)
    
    bd "Guia! Look!!! I've recovered my account!!! This time, I put a high-level security in it. It's not 'brent123' anymore."

    show bd masayaclose at left with dissolve:
        size(500, 646) yalign 1.2
    
    bd "But you know what I'm curious about? The hacker left a note."

    hide bd with dissolve

    show gf m at left with moveinleft:
        size(500, 646) xpos -80
    
    gf "Oh really? What does the note contain?"

    hide gf with dissolve
    
    show bd masayaopen at left with dissolve:
        size(500, 646)
    
    bd "I still don't know... I am scared it might be a virus or something that's why I waited for you."

    hide bd with dissolve
    
    show gf f at left with dissolve:
        size(500, 646) xpos -80
        
    gf "Open it! Maybe the hacker would reveal something there!!!"

    hide gf with dissolve
    
    show end note with dissolve:
        zoom 0.8 xalign 0.5 yoffset 0.2

    stop music fadeout 1.0

    play audio "audio/ring.ogg" fadein 1.0

    pause
    
    hide end note with dissolve

    "Brent Dackris wakes up to get ready for his first day as Student Council President..."

    scene bg end
    pause
    pause
    return