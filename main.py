from pathlib import Path

eol = '\n'
outputList = []
outputFile = open(Path(__file__).parent / "outputPS1.txt", "w+")


def read_input(input_file):
    prod_list = list()
    stage_list = list()
    photo_list = list()
    file_path = Path(__file__).parent / input_file
    if file_path.exists():
        input_text_file = open(file_path, "r")
        lines = input_text_file.readlines()
        count = 1
        for line in lines:
            # Strips the newline character
            print(f"Line{count}: {line.strip()}")
            count += 1
            # Split based on ':' to get the contents from the key
            line_info = line.strip().split(':')
            # Check each key and fetch their content
            if line_info[0].strip() == "Products":
                prod_list = [x.strip() for x in line_info[1].split('/')]
            elif line_info[0].strip() == "Staging":
                stage_list = [x.strip() for x in line_info[1].split('/')]
            elif line_info[0].strip() == "Photo":
                photo_list = [x.strip() for x in line_info[1].split('/')]
        # Finally, close file object after adding content to list
        input_text_file.close()
    return prod_list, stage_list, photo_list


def calculate_job_time(sb):
    tmp_stage = 0
    tmp_photo = 0
    idle_time = int(sb[0][0])
    photo_time = int(sb[0][2])
    total_photo_time = photo_time
    for item in sb[1:]:
        tmp_stage = tmp_stage + int(item[0])
        if tmp_stage < photo_time:
            tmp_photo = photo_time - tmp_stage
        elif tmp_stage > photo_time:
            idle_time = idle_time + tmp_stage - photo_time
            tmp_photo = 0
        elif tmp_stage == photo_time:
            tmp_photo = 0
        photo_time = tmp_photo + int(item[2])
        tmp_stage = 0
        total_photo_time = total_photo_time + int(item[2])
    total_time = total_photo_time + idle_time
    return idle_time, total_time


if __name__ == '__main__':
    input_files = ['inputPS1.txt', 'input1.txt', 'input2.txt', 'input3.txt', 'input4.txt']
    # input_files = ['inputPS1.txt']
    for each_input in input_files:
        outputList.append(eol)
        a, b, c = read_input(each_input)
        if len(a) is not 0:
            stage_times, product_seq, photo_times = zip(*sorted(zip(b, a, c)))
            job_zip = sorted(zip(b, a, c))
            idle, total = calculate_job_time(job_zip)
            print(f"Product Sequence: {product_seq}")
            outputList .append(f"Product Sequence: {product_seq}")
            print(f"Total time to complete photoshoot: {total}")
            outputList.append(f"Total time to complete photoshoot: {total}")
            print(f"Idle time for Xavier: {idle}")
            outputList.append(f"Idle time for Xavier: {idle}")
            print(f"Order of Algorithm : nlogn")
            outputList.append(eol)
            print(f"===================== END of {each_input} ==========================\n")
        else:
            print("INVALID File Name or Path")
    for out_lines in outputList:
        outputFile.write("%s\n" % out_lines)
    outputFile.close()
