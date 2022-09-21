def cut_xml_symbols(txt):
    op_txt = str(txt)
    op_txt = op_txt.replace('<CustomQuestions>', '').replace('</CustomQuestions>', '')\
        .replace('<CustomQuestion>', '').replace('</CustomQuestion>', '')\
        .replace('<Questions>', '').replace('</Questions>', '')\
        .replace('<Question>', '').replace('</Question>', '')\
        .replace('<Answers>', '').replace('</Answers>', '')\
        .replace('<Answer>', '').replace('</Answer>', '')\
        .replace('<CustomQuestionGroup>', '').replace('</CustomQuestionGroup>', '')\
        .replace('<CustomQuestionGroups>', '').replace('</CustomQuestionGroups>', '')\
        .replace('<CustomQuestionGroup name="Weapon Question">', '')\
        .replace('<CustomQuestionGroup name="DUI Questions">', '')\
        .replace('<CustomQuestionGroup name="Vehicle Questions">', '')
    op_txt2 = op_txt
    op_txt2 = op_txt2.replace('\n', ' ').replace('\t', ' ').strip(' ')
    op_txt2 = op_txt2.replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ')
    tab = op_txt2.split(' ')
    print(tab)
    print(len(tab))
    return tab


text = '''
<CustomQuestions>
  <CustomQuestion>
    <Question>Do you live in this neighborhood?</Question>
    <Answers>
      <Answer>Yes sir, I live with my grandma</Answer>
      <Answer>Why are you so curious?</Answer>
      <Answer>Nope</Answer>
      <Answer>No, I live up north</Answer>
    </Answers>
  </CustomQuestion>
  <CustomQuestion>
    <Question>Do you have warrant?</Question>
    <Answers>
      <Answer>Hell I know</Answer>
      <Answer>Maybe, from another state</Answer>
      <Answer>I can't remember</Answer>
      <Answer>You should check it for yourself</Answer>
    </Answers>
  </CustomQuestion>
  <CustomQuestionGroup name="DUI Questions">
    <CustomQuestion>
      <Question>When was the last time you drink?</Question>
      <Answers>
        <Answer>A couple hours ago</Answer>
        <Answer>I don't remember</Answer>
        <Answer>Just an hour ago</Answer>
        <Answer>Yesterday</Answer>
      </Answers>
    </CustomQuestion>
    <CustomQuestion>
      <Question>How much did you drink?</Question>
      <Answers>
        <Answer>A glass of wine</Answer>
        <Answer>Just 2 cans of beer</Answer>
        <Answer>A bottle of vodka</Answer>
        <Answer>Just a sip of bourbon</Answer>
      </Answers>
    </CustomQuestion>
    <CustomQuestion>
      <Question>Why are your eyes red?</Question>
      <Answers>
        <Answer>I'm so tired sir. I work 14 hours a day</Answer>
        <Answer>I think some dirt got into my eyes</Answer>
        <Answer>Do you think I'm drunk?</Answer>
        <Answer>Yeah my eyes are always red. I think it's normal</Answer>
      </Answers>
    </CustomQuestion>
  </CustomQuestionGroup>
  <CustomQuestionGroup name="Vehicle Questions">
    <CustomQuestion>
      <Question>Do you own that vehicle?</Question>
      <Answers>
        <Answer>Yes, that's mine</Answer>
        <Answer>I borrow my mother's vehicle</Answer>
        <Answer>Absolutely. Why do you ask?</Answer>
        <Answer>Yes. It's beautiful, isn't it?</Answer>
      </Answers>
    </CustomQuestion>
    <CustomQuestion>
      <Question>Do you know the registration has expired?</Question>
      <Answers>
        <Answer>I'm so sorry. I must have forgotten</Answer>
        <Answer>Really? I don't believe you</Answer>
        <Answer>Are you sure? I renewed it last month</Answer>
        <Answer>Sorry sir, I'll renew it as soon as possible</Answer>
      </Answers>
    </CustomQuestion>
    <CustomQuestion>
      <Question>Do you know the insurance has expired?</Question>
      <Answers>
        <Answer>I'm so sorry. I must have forgotten</Answer>
        <Answer>I don't believe you</Answer>
        <Answer>Are you sure? I renewed it last month</Answer>
        <Answer>Sorry sir, I'll renew it as soon as possible</Answer>
      </Answers>
    </CustomQuestion>
  </CustomQuestionGroup>
  <CustomQuestionGroup name="Narcotic Questions">
    <CustomQuestion>
      <Question>What is that white powder?</Question>
      <Answers>
        <Answer>I don't know what you're talking about</Answer>
        <Answer>I think it's just a salt</Answer>
        <Answer>Maybe cocaine. I'm not sure</Answer>
        <Answer>Mmm... what do you think it is?</Answer>
      </Answers>
    </CustomQuestion>
    <CustomQuestion>
      <Question>What is that white crystal?</Question>
      <Answers>
        <Answer>I don't know what you're talking about</Answer>
        <Answer>I think it's just a sugar</Answer>
        <Answer>Maybe meth. I'm not sure</Answer>
        <Answer>Mmm... what do you think it is?</Answer>
      </Answers>
    </CustomQuestion>
    <CustomQuestion>
      <Question>Are those needle marks on your arm?</Question>
      <Answers>
        <Answer>Those are bee stings</Answer>
        <Answer>It's just the I.V. marks</Answer>
        <Answer>What do you think it is?</Answer>
        <Answer>Yes, I also have them on my other parts</Answer>
      </Answers>
    </CustomQuestion>
  </CustomQuestionGroup>
  <CustomQuestionGroup name="Weapon Question">
    <CustomQuestion>
      <Question>Is this weapon stolen?</Question>
      <Answers>
        <Answer>I dunno. I bought it from pawn shop</Answer>
        <Answer>Why don't you check it in your system?</Answer>
        <Answer>It's legit. I have the receipt</Answer>
        <Answer>I'm not sure. I borrow it from my friend</Answer>
      </Answers>
    </CustomQuestion>
    <CustomQuestion>
      <Question>Why you don't have gun permit?</Question>
      <Answers>
        <Answer>I don't need it. Too expensive</Answer>
        <Answer>There's a mistake. I just got it a week ago</Answer>
        <Answer>I don't have time to get it</Answer>
        <Answer>Gun permit is only for rich people</Answer>
      </Answers>
    </CustomQuestion>
    <CustomQuestion>
      <Question>Do you have weapon on your person?</Question>
      <Answers>
        <Answer>No. I hate weapons</Answer>
        <Answer>Why don't you pat me down?</Answer>
        <Answer>Yes. Lots of it</Answer>
        <Answer>Might be. I forgot</Answer>
      </Answers>
    </CustomQuestion>
  </CustomQuestionGroup>
</CustomQuestions>

'''

cut_xml_symbols(text)

