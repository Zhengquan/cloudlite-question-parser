# CLoudLite Question Parser

Run and copy the output to the spreadsheet for importing questions.

## Usage

    ./parse.py sample_input.txt

## Format of Input

    ===
    难度：简单
    题型：单选
    描述：Question 1
    选项：
    A：Answer_A
    B：Answer_B
    C：Answer_C
    D：Answer_D
    正确答案：D
    答案解析：bla bla bla
    ===
    难度：简单
    题型：判断
    描述：Question 2
    正确答案：正确
    答案解析：
    ===
    难度：简单
    题型：多选
    描述：Question C
    选项：
    A：Anser_A
    B：Anser_B
    C：Anser_C
    D：Anser_D
    E：Anser_E
    正确答案：A，B，C，D，E
    答案解析：blablabla

## Sample Output

    Total number of questions:  3
    ******************
    Numer of  Simple  questions: 3
    Single Selection: 1
    Multiple Selection: 1
    True or False: 1
    ******************
    Numer of  Normal questions: 0
    Single Selection: 0
    Multiple Selection: 0
    True or False: 0
    ******************
    Numer of  Complex  questions: 0
    Single Selection: 0
    Multiple Selection: 0
    True or False: 0
    ******************
    ------------------
    1 	 1 	 Question 1 	 Answer_A	Answer_B	Answer_C	Answer_D		 	 D 	 bla bla bla
    3 	 1 	 Question 2 	 					 	 1
    2 	 1 	 Question C 	 Anser_A	Anser_B	Anser_C	Anser_D	Anser_E	 	 A,B,C,D,E 	 blablabla


## Convert Rules

    【题型】列取值：单选填1，多选填2，判断题填3。
    【难度】列取值：简单填1，普通填5，困难填10。
    【选项】列：对于判断题，选项空着不填即可。
    【正确答案】列：单选题填写正确选项，大写字母；多选题填写正确选项，大写字母，用逗号分隔；判断题正确填1，错误填0。
    【其他】选项为空或者不足6个选项，会自动填充至6列