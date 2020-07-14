from process_data.processing import process_data
step = 1

step_dict = {
    1: "process_data"
}


def main():
    step_func = step_dict.get(step)
    if step_func is "process_data":
        process_data()
    else:
        pass

if __name__ == '__main__':
    main()