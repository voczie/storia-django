from ctypes import sizeof
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import functions, models

def submit_form(request):
    if request.method == 'GET':
      return render(request, 'modelo/index.html')
    else:
      post_returns = request.POST.dict()

      example = functions.check_token(post_returns.get('text[]'))

      input_len = len(example.split())
      size = post_returns.get('length[]')
      temperature = post_returns.get('temperature[]')
    
      output = functions.query({"inputs": example,
                               "parameters": {'repetition_penalty': float(temperature), 'num_beams': 5,
                                              'no_repeat_ngram_size': 3, 'max_length': input_len + int(size)}})
      print(output)
      output_text = functions.remove_token(output[0].get('generated_text'))
      print(output_text)
      
      return render(request, 'modelo/index.html', {'texto': output_text})

def save_form(request):
      post_returns = request.POST.dict()

      text = post_returns.get('text[]')
      size = post_returns.get('length[]')
      temperature = post_returns.get('temperature[]')

      story = models.Story(example=text, size=int(size), temperature=float(temperature))
      story.save()
      print("StorIA registrada! ID: {}".format(story.id))

      return render(request, 'modelo/index.html')

# def load_storia(request, post_id):
#   if request.method == 'GET':
#     all_records = models.Story.objects.all()
#     actual_record = all_records[post_id]

#     actual_record_dict = {
#       'texto':actual_record.example
#     }

#     return render(request, 'modelo/storias.html', actual_record_dict)

def load_storia(request):
  all_records = models.Story.objects.all()
  page = request.GET.get('page', 1)

  paginator = Paginator(all_records, 1)

  try:
    records = paginator.page(page)
  except PageNotAnInteger:
    records = paginator.page(page)
  except EmptyPage:
    records = paginator.page(page)

  return render(request, 'modelo/storias.html', {'records': records})

def load_storias(request):
  all_records = models.Story.objects.all()
  page = request.GET.get('page', 1)

  paginator = Paginator(all_records, len(all_records))

  try:
    records = paginator.page(page)
  except PageNotAnInteger:
    records = paginator.page(page)
  except EmptyPage:
    records = paginator.page(page)

  return render(request, 'modelo/storiaspage.html', {'records': records})

def members(request):
  return render(request, 'modelo/members.html')

def social(request):
  return render(request, 'modelo/social.html')