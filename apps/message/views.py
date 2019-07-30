from django.shortcuts import render
from .models import UserMessage
# Create your views here.
def getform(request):
    # 1 从数据库提取出来所有数据
    # all_messages = UserMessage.objects.all()
    # # 默认的表 UserMessage.object有许多的方法
    # # UserMessage.objects.all() 将表内所有的数据都返回过来
    # for message in all_messages:
    #     print(message.name)

    # 2 从数据库提取出来特定成分的数据
    # all_messages = UserMessage.objects.filter(name='afrunk', address='北京')

    # 3 将数据保存在数据库中
    # user_message = UserMessage()
    # user_message.name = 'afrunk-csyz'
    # user_message.message = 'helloworld2'
    # user_message.address = '上海'
    # user_message.email = '2@2.com'
    # user_message.object_id = 'hellow'
    # user_message.save()
    # 将数据写入到数据表中

    # 4 将HTMl表单中的数据传递过来保存到数据库中
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = 'helloworld3'
        user_message.save()

    # 5 删除数据库中的数据
    # all_messages = UserMessage.objects.filter(name='afrunk-csyz', address='上海')
    # # all_messages.delete()#删除上面筛选出来的整个数据
    # for message in all_messages:
    #     message.delete()  # 删掉我们选出来的数据
    #     print(message.name)

    # 6 将数据库的数据展示在前端中
    message = None
    all_messages = UserMessage.objects.filter(name='afrunk')
    if all_messages:
        message = all_messages[0]
    return render(request,'message_form.html',{"my_message":message})


# 测试 git