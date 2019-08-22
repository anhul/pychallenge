from PythonChallenge1 import py_challenge_1

NUM_CHALL_COMPLETED = 2

#strings used for output formatting
link_to_next_chall = r"http://www.pythonchallenge.com/pc/def/{}.html"
challenge_header = 10*"=" + " Python challenge {} " + 10*"="
challenge_tail = 40*"="

#Lists wiht challenge results
challenge_results = []
link_keys = []

#Python challenge 0
challenge_result = 2 ** 38
challenge_results.append(challenge_result)
link_keys.append(challenge_result)

#Python challenge 1
encoded_string = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq "
                  "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw "
                  "rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq "
                  "pcamkkclbcb. lmu ynnjw ml rfc spj.")
challenge_result = py_challenge_1(encoded_string)
challenge_results.append(challenge_result)
link_keys.append(py_challenge_1("map"))

#Challenge results output
for index in range(NUM_CHALL_COMPLETED):

    print(challenge_header.format(index))
    print()
    print("Solution:")
    print(challenge_results[index])
    print()
    print("Link to the next challenge:")
    print(link_to_next_chall.format(link_keys[index]))
    print()
    print(challenge_tail)
    print()
