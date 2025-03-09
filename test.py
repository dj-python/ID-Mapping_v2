class Test:
    def __init__(self):
        self.model_name = None
        self.Decoding = None
        self.AFDriverSlave = None
        self.file_open = None
        self.All_Info_data = None
        self.open_model_data()

    def open_model_data(self):
        # model name display
        self.model_name = self.extract_info('Model Name :')
        print(self.model_name)

    def extract_info(self, text):
        with open('Sensor Info.txt', 'r', encoding='utf-8') as file_open:
            self.All_Info_data = file_open.readlines()

        for line in self.All_Info_data:
            line = line.strip()
            if text in line:
                start_index = line.index(text)
                extracted_value = line[start_index + len(text):].strip()
                if extracted_value:
                    return extracted_value
        return ''

if __name__ == "__main__":
    execute_test = Test()