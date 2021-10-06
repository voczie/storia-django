from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import functions

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

      output_text = functions.remove_token(output[0].get('generated_text'))
      print(output_text)
      
      return render(request, 'modelo/index.html', {'texto': output_text})
