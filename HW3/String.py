class String():
    def __init__(self,string: str ,rules=[]):
        self.string = str(string)
        self.rules = rules

    def __str__(self):
            return self.string

    def __len__(self):
        return len(self.string)

    def replace(self,old=None,new=None,count=100):
        return str(self.string).replace(old,new,count)

    def __add__(self, other):
        if isinstance(self,String) and isinstance(other,String):
            return String(str(self.string) + str(other.string),self.rules)
        elif isinstance(self,String) and isinstance(other,str):
            return String(str(self.string) +other,self.rules)
        elif isinstance(self,str) and isinstance(other,String):
            return String(self +str(other.string),self.rules)

    def __radd__(self, other):
        return String(self.string + other,self.rules)

    def __eq__(self, other):
        if isinstance(self,String) and isinstance(other,String):
            if str(self.string) == str(other.string):
                return True
            else:
                return False
        elif isinstance(self,String) and isinstance(other,str):
            if str(self.string) == other:
                return True
            else:
                return False

    def __mul__(self, other):
        return String(str(self.string)*other,self.rules)

    def __rmul__(self, other):
        return String(str(self.string)*other,self.rules)

    def isupper(self):
        if str(self.string).isupper():
            return True
        else:
            return False

    def islower(self):
        if str(self.string).islower():
            return True
        else:
            return False

    def count(self,substring,start= None,end=None):
        return str(self.string).count(substring,start,end)

    def __getitem__(self, subscript):
        if isinstance(subscript, slice):
            return self.string[subscript]
        else:
            return self.string[subscript]

    def __setitem__(self, subscript, item):
        self.string[subscript] = item

    def __delitem__(self, subscript):
        del self.rules[subscript]

    def base64(self) -> 'String': #TODO: exeption ot padding("=") chars
        '''
        Encode the String (self) to a base64 string
        :return: a new instance of String with the encoded string.
        '''
        copy = self
        if (copy.string[-1] == "="): #TODO: PADDING?
            copy = copy[-1]
        binary = "".join(format(ord(i),"08b") for i in str(copy.string))
        sequences  = []
        while binary != "":
            tmp = binary[:6]
            if len(tmp) < 6:
                while len(tmp) < 6:
                     tmp = tmp + "0"
            sequences.append(tmp)
            binary = binary[6::]
        chars_in64bit = []
        for cell in sequences: #turn to base64
             chars_in64bit.append(self.turn_to_64bit(cell))
        result = String("".join(chars_in64bit))
        return result
    base64_to_char = {
        "000000": "A", "010000": "Q", "100000": "g", "110000": "w", "000001": "B", "010001": "R", "100001": "h",
         "110001": "x", "000010": "C", "010010": "S", "100010": "i", "110010": "y", "000011": "D", "010011": "T",
         "100011": "j", "110011": "z", "000100": "E", "010100": "U", "100100": "k", "110100": "0", "000101": "F",
        "010101": "V", "100101": "l", "110101": "1", "000110": "G", "010110": "W", "100110": "m", "110110": "2",
        "000111": "H", "010111": "X", "100111": "n", "110111": "3", "001000": "I", "011000": "Y", "101000": "o",
        "111000": "4", "001001": "J", "011001": "Z", "101001": "p", "111001": "5", "001010": "K", "011010": "a",
        "101010": "q", "111010": "6", "001011": "L", "011011": "b", "101011": "r", "111011": "7", "001100": "M",
        "011100": "c", "101100": "s", "111100": "8", "001101": "N", "011101": "d", "101101": "t", "111101": "9",
        "001110": "O", "011110": "e", "101110": "u", "111110": "+", "001111": "P", "011111": "f", "101111": "v",
        "111111": "/" }

    def turn_to_64bit(self,binary_form):
        val = self.base64_to_char[binary_form]
        return val
        pass


    def byte_pair_encoding(self) -> 'String':
        '''
        Encode the String (self) to a byte pair string
        :return: a new instance of String with the encoded string.
        :exception: BytePairError
        '''
        copy  = self.string
        usable_groups = self.get_usable_groups()
        list_of_usable_values = []
        value_dictionary = {"Other": [33,34	,35,36,37,38,39,40,41,42,43,44,45,46,47,58,59,60,61,62,63,64,91,92,93,94,95,96,124,125,126],
                            "Digits": [48,49,50,51,52,53,54,55,56,57],
                            "Upper case": [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90],
                            "Lower case": [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]}
        for group in usable_groups:
            list_of_usable_values.extend(value_dictionary[group])
        pairs_repetitions = self.count_pairs(copy)
        changing_rules = []
        while max(pairs_repetitions.values()) > 1:
            max_pair = String(max(pairs_repetitions, key=lambda x: pairs_repetitions[x]))
            changed_value,list_of_usable_values,new_rule = max_pair.switch(list_of_usable_values)
            changing_rules.append(new_rule)
            copy = copy.replace(max_pair.string,changed_value)
            pairs_repetitions = self.count_pairs(copy)
        res = String(copy,changing_rules)
        return res



    def switch(self,list_of_values):
        if list_of_values == []:
            raise BytePairError
        old_pair = self
        new_char = str(chr(list_of_values[0]))
        add_to_rules = new_char + " = " + old_pair.string
        list_of_values = list_of_values[1:]
        return new_char, list_of_values, add_to_rules

    def get_usable_groups(self):
        list_of_char = list(self)
        Group_types = []
        able_to_use_groups = ["Other","Digits","Upper case", "Lower case"]
        for char in list_of_char:
            ascii_value = ord(char)
            if  97 <= ascii_value <= 122 :
                Group_types.append("Lower case")
            elif 65 <= ascii_value <= 90:
                Group_types.append("Upper case")
            elif 48 <= ascii_value <= 57:
                Group_types.append("Digits")
            elif (33 <= ascii_value <= 47) or (58 <= ascii_value<=64) or (91<=ascii_value<=96) or (124 <= ascii_value <= 126):
                Group_types.append("Other")
            else:
                raise BytePairError
        [able_to_use_groups.remove(x) for x in Group_types if x in able_to_use_groups]
        if able_to_use_groups == []:
            raise BytePairError
        return able_to_use_groups

    def count_pairs(self,string):
        copy = string
        pairs_repetitions= {}
        while len(copy) > 1:
            current_pair = copy[:2]
            if current_pair in pairs_repetitions.keys():
                copy = copy[1:]
                continue
            num_of_repetitions = copy[2:].count(current_pair) + 1
            pairs_repetitions[current_pair] = num_of_repetitions
            copy = copy[1:]
        return pairs_repetitions

    def cyclic_bits(self, num: int = 0) -> 'String':
        '''
        Encode the String (self) to a cyclic bits string
        :return: a new instance of String with the encoded string.
        '''
        copy = self
        list_of_chars = list(copy)
        list_of_binars = []
        for i in range(len(list_of_chars)):
            list_of_binars.append(format(ord(list_of_chars[i]),"08b"))
        long_binary = "".join(list_of_binars)
        long_binary = self.shift_binar(long_binary,num)
        binar_list = []
        while long_binary != "":
            binar_list.append(long_binary[:8])
            long_binary = long_binary[8:]
        result_list = []
        for k in range(len(binar_list)):
            temp = int(binar_list[k], 2)
            temp = chr(temp)
            result_list.append(temp)
        return String("".join(result_list))

    def shift_binar(self, binary_num,num):
        substring_index = num
        while substring_index > len(binary_num):
            substring_index = substring_index - len(binary_num)
        shifted_binar = binary_num[substring_index:] + binary_num[:substring_index]
        return shifted_binar

    def cyclic_chars(self, num: int = 0) -> 'String': #TODO: what can go wrong?
        '''
        Encode the String (self) to a cyclic chars string
        :return: a new instance of String with the encoded string.
        :exception: CyclicCharsError
        '''
        list_of_chars = []
        copy = self
        while num > 94:
            num = num-95
        while num < -94:
            num = num +95
        for i in range(len(copy)):
            list_of_chars.append(copy[i])
        list_of_Ascii_values = []
        for i in range(len(list_of_chars)):
            list_of_Ascii_values.append(ord(list_of_chars[i]))
        for i in range(len(list_of_Ascii_values)):
            if ( list_of_Ascii_values[i] < 32 ) or (list_of_Ascii_values[i] > 126):
                raise CyclicCharsError
            list_of_Ascii_values[i] = list_of_Ascii_values[i] +num
            if list_of_Ascii_values[i] > 126:
                list_of_Ascii_values[i] = list_of_Ascii_values[i] - 126 +32 -1
            elif list_of_Ascii_values[i] < 32:
                list_of_Ascii_values[i] = list_of_Ascii_values[i] + 126 - 32 +1
        list_after_cycling = []
        for i in range(len(list_of_Ascii_values)):
            list_after_cycling.append(chr(list_of_Ascii_values[i]))
        cycled_val = "".join(list_after_cycling)
        return String(cycled_val)

    def histogram_of_chars(self) -> dict:
        '''
        calculate the histogram of the String (self). The bins are
        "control code", "digits", "upper", "lower" , "other printable"
        and "higher than 128".
        :return: a dictonery of the histogram. keys are bins.
        '''
        copy = self.string
        dictionary = {"control code":0 , "digits": 0,"upper": 0 , "lower": 0 , "other printable": 0,
                      "higher than 128": 0}
        list_of_ord = [ord(i) for i in copy ]
        for char in list_of_ord:
            if 97 <= char <= 122:
                dictionary["lower"]+=1
            elif 65 <= char <= 90:
                dictionary["upper"] +=1
            elif 48 <= char <= 57:
                dictionary["digits"] +=1
            elif (32 <= char <= 47) or (58 <= char <= 64) or (91 <= char <= 96) or (
                    123 <= char <= 126): #TODO: is 123 should be here or leave 124 instead
                dictionary["other printable"] +=1
            elif 128 <= char <= 255:
                dictionary["higher than 128"] +=1
            elif (0<= char <= 31)  or (char == 127): #TODO: should i add 127 here?
                dictionary["control code"]+=1
        return dictionary

    char_to_64bit = {v:k for k , v in base64_to_char.items()}

    def decode_base64(self) -> 'String': #TODO: raise exeption when not decodable
        '''
        Decode the String (self) to its original base64 string.
        :return: a new instance of String with the endecoded string.
        :exception: Base64DecodeError
        '''
        chars = []
        copy = self
        while len(copy) > 0:
            chars.append(copy[:1])
            copy = copy[1:]
        long_binar = ""
        for cell in chars:
            if cell not in self.base64_to_char.values():
                raise Base64DecodeError
            tmp = String.char_to_64bit[cell]
            long_binar = long_binar +tmp
        # if len(long_binar)+1 % 8:
        #     raise Exception("Base64DecodeError") #TODO: does the lenght of the binar can riase exeption?
        listof8 = []
        while long_binar != "":
            listof8.append(long_binar[:8])
            long_binar = long_binar[8:]
        result_list = []
        if len(listof8[-1]) <8 :
            listof8 = listof8[:-1]
        for k in range(len(listof8)):
            temp = int(listof8[k],2)
            temp = chr(temp)
            result_list.append(temp)
        result = "".join(result_list)
        return String(result)

    def decode_byte_pair(self) -> 'String':
        '''
        Decode the String (self) to its original byte pair string.
        Uses the property rules.
        :return: a new instance of String with the endecoded string.
        :exception: BytePairDecodeError
        '''
        copy = self.string
        rules_to_use = self.rules
        if rules_to_use == []:
            raise BytePairDecodeError
        rules_to_use = rules_to_use[::-1]
        i=0
        while len(rules_to_use) > 0:
            tmp_list = rules_to_use[0].split(" = ")
            char = tmp_list[0]
            pair = tmp_list[1]
            if char not in copy:
                raise BytePairDecodeError
            copy = copy.replace(char,pair)
            rules_to_use = rules_to_use[1:]
            i = i+1
        res = String(copy)
        return res


    def decode_cyclic_bits(self, num: int = 0) -> 'String':
        '''
        Decode the String (self) to its original cyclic bits string.
        :return: a new instance of String with the endecoded string.
        '''
        copy = self
        list_of_chars = list(copy)
        list_of_binars = []
        for i in range(len(list_of_chars)):
            list_of_binars.append(format(ord(list_of_chars[i]), "08b"))
        long_binary = "".join(list_of_binars)
        long_binary = self.shift_binar_reverse(long_binary, num)
        binar_list = []
        while long_binary != "":
            binar_list.append(long_binary[:8])
            long_binary = long_binary[8:]
        result_list = []
        for k in range(len(binar_list)):
            temp = int(binar_list[k], 2)
            temp = chr(temp)
            result_list.append(temp)
        return String("".join(result_list))

    def shift_binar_reverse(self, binary_num,num):
        substring_index = num
        while substring_index > len(binary_num):
            substring_index = substring_index - len(binary_num)
        shifted_binar = binary_num[-substring_index:] + binary_num[:-substring_index]
        return shifted_binar
        pass


    def decode_cyclic_chars(self, num: int = 0) -> 'String':
        '''
        Decode the String (self) to its original cyclic chars string.
        :return: a new instance of String with the endecoded string.
        :exception: CyclicCharsDecodeError
        '''
        copy = self
        list_of_chars = []
        while num > 94:
            num = num-95
        while num < -94:
            num = num +95
        for i in range(len(copy)):
            list_of_chars.append(copy[i])
        list_of_Ascii_values = []
        for i in range(len(list_of_chars)):
            list_of_Ascii_values.append(ord(list_of_chars[i]))
        for i in range(len(list_of_Ascii_values)):
            if ( list_of_Ascii_values[i] < 32 ) or (list_of_Ascii_values[i] > 126):
                raise CyclicCharsDecodeError
            list_of_Ascii_values[i] = list_of_Ascii_values[i]  - num
            if list_of_Ascii_values[i] < 32:
                list_of_Ascii_values[i] = list_of_Ascii_values[i] + 126 - 32 +1
            elif list_of_Ascii_values[i] > 126:
                list_of_Ascii_values[i] = list_of_Ascii_values[i] -126 +32 -1
        list_after_cycling = []
        for i in range(len(list_of_Ascii_values)):
            list_after_cycling.append(chr(list_of_Ascii_values[i]))
        cycled_val = String("".join(list_after_cycling))
        return cycled_val

class Base_Error_class(Exception):
    pass

class BytePairDecodeError(Base_Error_class):
    pass

class Base64DecodeError(Base_Error_class):
    pass

class CyclicCharsError(Base_Error_class):
    pass

class CyclicCharsDecodeError(Base_Error_class):
    pass

class BytePairError(Base_Error_class):
    pass

