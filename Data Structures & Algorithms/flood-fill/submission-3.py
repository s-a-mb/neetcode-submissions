class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        color_init = image[sr][sc]

        if color_init == color:
            return image

        image_width = len(image)

        image_height = len(image[0])




        def recursion( current_y, current_x ):

            if current_y >= image_width or current_x >= image_height or image[current_y][current_x] != color_init or current_y < 0 or current_x < 0:
                return

            image[current_y][current_x] = color
            
            recursion(current_y + 1, current_x) #south
            recursion(current_y - 1, current_x)#north
            recursion(current_y, current_x + 1)#east
            recursion(current_y, current_x - 1)#weast

        recursion(sr, sc)

        return image

        





        