class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f'your name is {self.name} and Id is {self.username}')

    def __repr__(self):
        return f'{self.name} is {self.username}'


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
    
    def __str__(self):
        return f'{self.author} post this {self.title}'
    

posts =[]
post1 = Member('woojin', 'id', '123')
post2 = Member('second', 'weirj', '1233')
post3 = Member('third', 'wekihrkf', '1323')
posts.append(post1)
posts.append(post2)
posts.append(post3)
post4 = Member('woojin', 'id', '123')
post5 = Member('second', 'weirj', '1233')
post6 = Member('third', 'wekihrkf', '1323')
posts.append(post4)
posts.append(post5)
posts.append(post6)
post7 = Member('woojin', 'id', '123')
post8 = Member('second', 'weirj', '1233')
post9 = Member('third', 'wekihrkf', '1323')
posts.append(post7)
posts.append(post8)
posts.append(post9)

print(posts)