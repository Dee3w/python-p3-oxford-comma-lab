def oxford_comma(items):
     if len(items) == 1:
        return items[0]
     elif len(items) == 2:
        return " and ".join(items)
     elif len(items) > 2:
        new_list = items
        a = 'and ' + str(new_list[-1])
        new_list[-1] = a
        return ", ".join(new_list)
     else:
        return "List provided is empty."
