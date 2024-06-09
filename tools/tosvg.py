import argparse

from cglib.type import numpy_contour_to_data_structure, data_structure_to_svg



if __name__ == '__main__': 
    
    parser = argparse.ArgumentParser()
    parser.add_argument("input_filename", 
                        help= "File in .npy format containing the scalar field to be displayed. ", 
                        type = str) 
    parser.add_argument("datatoexport", 
                        help = "contour or cycle", 
                        type= str)
    
    args = parser.parse_args()
    file_name = args.input_filename
    datatoexport = args.datatoexport 

    if datatoexport == "contour": 
        
        try: 
            #import the graph 
            points, previous_edge, next_edge, cycle_index, cycles =\
                  numpy_contour_to_data_structure(file_name + "_contour")
            #create a svg file 
            data_structure_to_svg(points, 
                                  next_edge, 
                                  cycles, 
                                  file_name+ "_contour")
        except FileNotFoundError: 
            print("Please run the main tool before exporting the isocontours in SVG format.")
    
    elif datatoexport == "cycle": 

        try: 
            #import the graph with a single cycle
            points, previous_edge, next_edge, cycle_index, cycles =\
                  numpy_contour_to_data_structure(file_name + "_cycle")
            #create a svg file      
            data_structure_to_svg(points, 
                                  next_edge, 
                                  cycles, 
                                  file_name+ "_cycle")
        except FileNotFoundError: 
            print("Please run the main tool before exporting the cycle in SVG format.") 

    else: 
        print("Wrong argument, please enter either cycle or contour.")