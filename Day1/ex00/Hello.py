ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"
ft_tuple = (ft_tuple[0], "France!")
ft_set.remove("tutu!")
ft_set.add("Le Havre!")
ft_dict["Hello"] = "42 Le Havre!"

print(ft_list)
print(ft_tuple)
print(ft_set) # Order is not guaranteed on sets
print(ft_dict)