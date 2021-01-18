#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import re


questions = []

def main():
    file_path = sys.argv[1]

    if not os.path.isfile(file_path):
        print("File path {} does not exist. Exiting...".format(file_path))
        sys.exit()

    with open(file_path) as fp:
        parsed_question = {}
        for line in fp:
            process_line(line, parsed_question)

    print_question_summary()
    print("------------------")
    print_result()

def print_question_summary():
    print("Total number of questions:", len(questions))

    print("******************")
    print_summary_of_by_difficulty("Simple", 1)
    print_summary_of_by_difficulty("Normal", 5)
    print_summary_of_by_difficulty("Complex", 10)

def print_summary_of_by_difficulty(q_type_name, q_difficulty_code):
    filtered_questions = filterTheList(questions, lambda q: q["q_difficulty"] == q_difficulty_code)

    print("Numer of ", q_type_name, " questions:", len(filtered_questions))
    print("Single Selection:", len(list(filter(lambda q: q["q_type"] == 1, filtered_questions))))
    print("Multiple Selection:", len(list(filter(lambda q: q["q_type"] == 2, filtered_questions))))
    print("True or False:", len(list(filter(lambda q: q["q_type"] == 3, filtered_questions))))
    print("******************")


def filterTheList(list_obj, callback):
    new_list = list()
    # Iterate over all the items in dictionary
    for item in list_obj:
        # Check if item satisfies the given condition then add to new dict
        if callback(item):
            new_list.append(item)
    return new_list


def print_result():
    for question in questions:
        print(
            question["q_type"],
            "\t",
            question["q_difficulty"],
            "\t",
            question["q_desc"],
            "\t",
            build_options(question["q_options"]),
            "\t",
            question["q_answers"],
            "\t",
            question["q_answer_explanation"],
            sep=''
        )

def build_options(options):
    for i in range(6 - len(options)):
        options.append("")
    return "\t".join(options)

def process_line(line, parsed_question):
    if '===' in line:
        parsed_question = {}

    if line.startswith("难度"):
        process_difficulty(line, parsed_question)

    if line.startswith("选项"):
        parsed_question["q_options"] = []

    if line.startswith("题型"):
        process_quesiton_type(line, parsed_question)

    if line.startswith("描述"):
        process_quesiton_desc(line, parsed_question)

    if re.search(r"^[A-Z|a-z][:|：]", line):
        process_answer_options(line, parsed_question)

    if line.startswith("正确答案"):
        process_answers(line, parsed_question)

    if line.startswith("答案解析"):
        process_answer_explanation(line, parsed_question)
        questions.append(parsed_question.copy())
        parsed_question["q_options"] = []


def process_answer_options(line, parsed_question):
    captured_group = re.search("^[A-Z|a-z][:|：](.+)", line).group(1).strip()
    parsed_question["q_options"].append(captured_group)


def process_answers(line, parsed_question):
    parsed_line = line.replace('，', ',')
    correct_answer = re.search("^正确答案[：|:](.+)", parsed_line).group(1).upper().strip()
    if parsed_question["q_type"] == 3:
        answer_code_dict = {"正确": 1, "错误": 0}
        correct_answer = answer_code_dict[correct_answer]

    parsed_question["q_answers"] = correct_answer

def process_answer_explanation(line, parsed_question):
    anser_exp = re.search("^答案解析[：|:](.+)", line)
    if anser_exp is None:
        parsed_question["q_answer_explanation"] = ""
    else:
        parsed_question["q_answer_explanation"] = anser_exp.group(1).strip()


def process_quesiton_desc(line, parsed_question):
    captured_group = re.search("^描述[：|:](.+)", line).group(1).strip()
    parsed_question["q_desc"] = captured_group


def process_quesiton_type(line, parsed_question):
    #  单选填1，多选填2，判断题填3
    difficulty_dict = {"单选": 1, "多选": 2, "判断": 3}
    captured_group = re.search("^题型[：|:](.+)", line).group(1)
    parsed_question["q_type"] = difficulty_dict[captured_group]


def process_difficulty(line, parsed_question):
    # 简单填1，普通填5，困难填10
    difficulty_dict = {"简单": 1, "普通": 5, "困难": 10}
    captured_group = re.search("^难度[：|:](.+)", line).group(1)
    parsed_question["q_difficulty"] = difficulty_dict[captured_group]


if __name__ == '__main__':
    main()
