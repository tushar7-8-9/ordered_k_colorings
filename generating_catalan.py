"""
Generating Catalan k-Colorings of size n
Note - 1. Size I am using numbers to denote the colors, the funtion only works for upto 9 colors. 
This can we easy fixed by using a seperate naming scheme for the colors. 
2. If i > j then Color i < Color j. For exmaple, Color 1 > Color 2.
"""

def main(n: int, k: int):
    def generate(counter: list, cur_graph: str):
        if len(cur_graph) == n: 
            append = True
            for i in range(0, k): 
                if counter[i] != counter[i - 1]: append = False
            if append: all_graphs.append(cur_graph)
            return 
    
        #conditional to add color 1 edge 
        if counter[0] < n - (k - 1): 
            new_counter = counter.copy()
            new_counter[0] += 1
            generate(new_counter, cur_graph + '1')
        
        #conditional to add color >1 edges   
        for i in range(1, k):
            if counter[i] < n - (k - 1) and counter[i] < counter[i - 1]:
                new_counter = counter.copy()
                new_counter[i] += 1
                generate(new_counter, cur_graph + str(i + 1))

    all_graphs = []
    generate([0 for i in range(0,k)], '')
    return all_graphs


if __name__ == "__main__":
    n = 10 #No. of edges in the graph
    k = 5 #No. of Colors
    print(main(n, k))
