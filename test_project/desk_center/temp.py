

#项目页面
"""
def task_project(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:

        print("进入任务")

        if request.method == "POST":
            dat = json.loads(request.body)
        if request.method == "GET":
            pass
        ret = {"success":"添加成功"}
        return HttpResponse(json.dumps(ret))
        # task_pro = models.task_projects.objects.all()
        # return render(request, "task_projects.html", locals())
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')

    """