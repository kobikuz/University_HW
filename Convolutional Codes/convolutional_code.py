class Node():
    def __init__(self,from_point,level,dictionary_of_nodes):
        self.zero = None
        self.one = None
        self.father = None
        self.from_point= from_point
        self.distance = None
        self.data = "" #what i will output in the end
        self.level = level
        self.dictionary_of_nodes = dictionary_of_nodes
        if dictionary_of_nodes != None:
            dictionary_of_nodes[from_point+str(self.level)] = self
        # print(from_point,level)


class generator:
    def __init__(self, polinom):
        self.relevant_indexes = [polinom[i:i + 1] for i in range(len(polinom))]


    def operation(self, binary_num):
        binary_num = str(binary_num)
        result_b4_modulo = 0
        relevant_len = len(self.relevant_indexes)
        for i in range(relevant_len):
            result_b4_modulo = result_b4_modulo + int(self.relevant_indexes[relevant_len - i - 1]) * int(binary_num[i])
        result = result_b4_modulo % 2
        return result

    def operation_plz_dont_crash(self, binary_num):
        binary_num = str(binary_num)
        result_b4_modulo = 0
        relevant_len = len(self.relevant_indexes)
        for i in range(relevant_len):
            result_b4_modulo = result_b4_modulo + int(self.relevant_indexes[i]) * int(binary_num[i])
        result = result_b4_modulo % 2
        return result




class ConvolutionalCode:
    def __init__(self, generators: tuple):
        self.delay = [i for i in generators]
        self.nedded_lenght , self.operators = self.find_operators(self.delay)
        self.generators = [generator(i) for i in self.operators]
        """
        :param generators: each element in the tuple represents a single generator polynomial. The convention
        we use is: 1+D=b011=3 (and not 1+D=6)
        """
        pass

    def find_operators(self,list_of_nums):
        full_binary_rep = [format(i, "08b") for i in list_of_nums]
        short_rep = []
        max_len = 0
        for i in full_binary_rep:
            i_index = i.index("1")
            k = i[i_index:]
            if max_len < len(k):
                max_len = len(k)
            short_rep.append(k)
        return (max_len-1),[binar.zfill(max_len) for binar in short_rep]

    def encode(self, data: bytes)  : #TODO: list missing
        """
        encode input data bytes. Uses zero tail termination

        :param data: data to be encoded
        :return: encoded data
        :rtype: list[int]
        """
        #)
        input = "".join([format(ord(chr(i)),"08b") for i in data])
        padded_input = (self.nedded_lenght * "0")+ str(input) + (self.nedded_lenght * "0")
        encoded_lst=[]
        for i in  range(len(padded_input)-self.nedded_lenght):
            for worker in self.generators:
               encoded_lst.append(worker.operation_plz_dont_crash(padded_input))
            padded_input = padded_input[1:] # here i move by 1
        return encoded_lst
        pass

    def decode(self, data) -> (bytes, int):
        """
        decode data bytes. The function assumes initial and final state of encoder was at the zero state.

        :param data: coded data to be decoded, list of ints representing each received bit.
        :return: return a tuple of decoded data, and the amount of corrected errors.
        :rtype: (bytes, int)
        """
        dictionary_of_nodes={}
        Dora_the_Explora,num_in_a_couple = self.map() #TODO:check
        amount_of_couples = len(self.generators)
        couples_string = [str(i) for i in data]
        couples = [(couples_string[amount_of_couples*i:amount_of_couples*i+amount_of_couples]) for i in range(len(data) // amount_of_couples)] #TODO:how many ints in a couple!
        couples_f = []
        for i in range(len(couples)):
            couples_f.append("".join(couples[i]))
        num_of_levels = len(couples_f)  #root is lv0
        root_from_point = "0"*self.nedded_lenght #I CAN SEE BY THE ROOT HOW MANY BITFLIPS I HAVE
        # root_from_point = "00"
        root = Node(root_from_point,0, dictionary_of_nodes)
        self.build_tree(num_of_levels,root,Dora_the_Explora)
        # print("tree is built")
        #self.print_tree(root)
        self.calculate_min_distances(root,Dora_the_Explora,couples_f,None)
        # print("min distance calculated")
        #self.print_tree(root)
        even_better_node = self.find_best_route_no_rec(dictionary_of_nodes,num_of_levels)
        decoded_msg = self.turn_to_decoded_msg(even_better_node.data)
        return (decoded_msg,even_better_node.distance)
        pass

    def turn_to_decoded_msg(self,inp):
        result = bytes(int(inp[i:i+8],2)for i in range(0,len(inp)-self.nedded_lenght,8))
        return result

    def find_best_route_no_rec(self,dictionary_of_nodes,num_of_levels):
        all_final_nodes = [node for node in dictionary_of_nodes.values() if node.level == num_of_levels]

        best_node = all_final_nodes[0]
        for node in all_final_nodes:
            if node.distance < best_node.distance:
                best_node = node
        print(self.print_node(best_node))
        return best_node

    # def find_best_route(self,curr_node,best_node,num_of_levels):
    #     if curr_node.level == num_of_levels :
    #         if curr_node.distance <= best_node.distance:
    #             return curr_node
    #         else:
    #             return best_node
    #     if curr_node.zero != None:
    #         best_node0 = self.find_best_route(curr_node.zero,best_node,num_of_levels)
    #         if best_node0.distance < best_node.distance:
    #             best_node = best_node0
    #     if curr_node.one != None:
    #         best_node1 = self.find_best_route(curr_node.one,best_node,num_of_levels)
    #         if best_node1.distance < best_node.distance:
    #             best_node = best_node1
    #     return best_node

    def calculate_min_distances(self,node,map,couples,father,direction=None):
        if node == None:
            return
        father_distance = 0
        curr_distance = 0
        my_data = ""
        if father != None:
            father_distance = father.distance
            curr_distance= self.calc_hamming_distance(couples,map,node,direction,father) + father_distance
            my_data = father.data+direction
        if node.distance == None :
            node.distance = curr_distance
            node.father = father
            node.data = my_data
            self.calculate_min_distances(node.zero,map,couples,node,"0")
            self.calculate_min_distances(node.one, map, couples, node,"1")
        elif  node.distance >= curr_distance:
            node.distance = curr_distance
            node.father = father
            node.data =my_data
            self.calculate_min_distances(node.zero, map, couples, node,"0")
            self.calculate_min_distances(node.one, map, couples, node,"1")
        return
        pass

    def calc_hamming_distance(self,couples,map,node,direction,father):
        exepected_val = map[direction+father.from_point][3]
        distance = 0
        try:
            for i in range(len(couples[0])):
                if couples[node.level-1][i] != exepected_val[i]: #TODO: MAYBE LV =-1
                    distance  = distance + 1
        except:
            print("ha!")
        return distance
        pass

    def build_tree(self,hight,curr_node,map):
        if curr_node.level >= hight:
            return curr_node
        child_key = map["0"+curr_node.from_point][1]
        if child_key+str(curr_node.level+1) not in curr_node.dictionary_of_nodes.keys():
            curr_node.zero = Node(child_key,curr_node.level+1,curr_node.dictionary_of_nodes)
            self.build_tree(hight,curr_node.zero,map)
        else:
            curr_node.zero = curr_node.dictionary_of_nodes[child_key+str(curr_node.level+1)]
        child_key = map["1" + curr_node.from_point][1]
        if child_key+str(curr_node.level+1) not in curr_node.dictionary_of_nodes.keys():
            curr_node.one = Node(map["1"+curr_node.from_point][1],curr_node.level+1,curr_node.dictionary_of_nodes)
            self.build_tree(hight,curr_node.one,map)
        else:
            curr_node.one = curr_node.dictionary_of_nodes[child_key+str(curr_node.level+1)]
        return curr_node

    def print_tree(self,root):
        print("+", self.print_node(root))
        childs = ""
        if root.zero != None:
            childs = childs + "     0: "+self.print_node(root.zero)
        if root.one != None:
            childs = childs + "     1: "+self.print_node(root.one)
        if childs != "":
            print(childs)
        if root.zero != None:
            self.print_tree(root.zero)
        if root.one != None:
            self.print_tree(root.one)

    def print_node(self,node):
        return "from_point: "+node.from_point+ " level: "+ str(node.level)+ " distance: "+ str(node.distance)+" data:" +str(node.data)
        pass

    def map(self): ##tmp = from,to,input,output
        #amount_of_generators = len(self.delay)
        starting_ponts = self.get_binary_options(2**(self.nedded_lenght)) #not amount but max lenght
        amount_of_options =abs(self.nedded_lenght - len(starting_ponts[0]))+1
        options = self.get_binary_options(amount_of_options+1)
        dict_map ={}
        for pont in starting_ponts:
            for opt in options:
                output = ""
                for worker in self.generators:
                    tmp=opt+pont
                    output = output+str(worker.operation(tmp))
                    dict_map[tmp]=[pont,tmp[:-1],opt,output] #tmp = from,to,input,output
        # print(dict_map)
        return dict_map,len(options)
        pass

    def get_binary_options(self,amount_of_generators):
        short_rep = []
        full_binary_rep = [format(i, "08b") for i in range((amount_of_generators))]
        max_len = 0
        for i in full_binary_rep:
            if int(i) ==0:
                short_rep.append("0")
            else:
                i_index = i.index("1")
                k = i[i_index:]
                if max_len < len(k):
                    max_len = len(k)
                short_rep.append(k)
        starting_points = [binar.zfill(max_len) for binar in short_rep]
        return starting_points



