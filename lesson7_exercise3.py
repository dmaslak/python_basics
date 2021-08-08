class MulticellularOrganism:
    def __init__(self, number_of_cells = 2):
        self.number_of_cells = number_of_cells
    
    def __add__(self, other):
        return self.number_of_cells + other.number_of_cells
    
    def __sub__(self, other):
        if self.number_of_cells > other.number_of_cells:
            return self.number_of_cells - other.number_of_cells
        else:
            print(f'The resulting organism\'s number of cells can\'t be less than or equal to zero.')

    def __mul__(self, other):
        new_organism = MulticellularOrganism(number_of_cells = self.number_of_cells * other.number_of_cells)
        return new_organism

    def __truediv__(self, other):
        new_organism = MulticellularOrganism(number_of_cells = self.number_of_cells // other.number_of_cells)
        return new_organism

    def make_order(self, cells_per_row):
        number_of_rows = self.number_of_cells // cells_per_row
        last_row = self.number_of_cells % cells_per_row

        for i in range(number_of_rows):
            print('*' * cells_per_row)
        print('*' * last_row)
        


org_1 = MulticellularOrganism(number_of_cells = 25)
org_2 = MulticellularOrganism(number_of_cells = 7)

org_1.make_order(10)
