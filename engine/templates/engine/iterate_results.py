for content in listings:
    title = content.find(class_='result-title').text
    description = content.find(class_='result-description').text
    link = content.find(class_='result-link').text
    url = content.find(class_='result-url').text
    results.append((title,description,url))
context = {
    'results':results
}
return render(request, 'engine/results.html', context)