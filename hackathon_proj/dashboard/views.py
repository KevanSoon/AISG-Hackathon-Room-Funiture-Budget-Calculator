from django.shortcuts import render, redirect
from django.views.generic import View
from tagui import run
from .models import Room,Funiture
from .forms import AddRoomForm, UpdateImageForm
import rpa as r
from peekingduck.runner import Runner
from peekingduck.pipeline.nodes.input import recorded
from peekingduck.pipeline.nodes.model import yolo, efficientdet
from peekingduck.pipeline.nodes.draw import bbox, group_bbox_and_tag
from peekingduck.pipeline.nodes.dabble import bbox_count
from peekingduck.pipeline.nodes.output import media_writer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from datetime import datetime



class Index(View):
    def get(self,request, *args, **kwargs):
        return render(request,'index.html')

#view dashboard page
class DashboardView(LoginRequiredMixin, View): 
   
    def get(self,request,*args,**kwargs):
        
        
        rooms = Room.objects.filter(user=request.user)

        

        return render(request, 'chart.html', {
        'rooms': rooms
    })
   
#Add a new room
class AddRoomsView(LoginRequiredMixin, View): 
   
    def get(self,request,*args,**kwargs):

        addroom_message = None

        if 'addroom_errormessage' in request.session:
                addroom_message = request.session['addroom_errormessage']
                del request.session['addroom_errormessage']
        
        rooms = Room.objects.filter(user=request.user)
       
        
        context = {
            "error_message": addroom_message,
            "rooms": rooms
        }

        return render(request, 'add_rooms.html', context)


    def post(self,request,*args,**kwargs):
        
        form = AddRoomForm(request.POST, request.FILES)
        files = request.FILES.getlist('room_image')


        if not files:
                error_message = "Cannot add new room, no room image was found"
                request.session['addroom_errormessage'] = error_message
                return redirect('dashboard:add-rooms')

        print(files)

        if form.is_valid():
            new_room = form.save(commit=False) 
            new_room.user = request.user
            

            new_room.save()

            for f in files:
                
                new_room.image = f
                
                     

            new_room.save()

        print(new_room.room_type)
        file_str = str(f)
        
        print(file_str)
        
      

        #peekingduck for Living Room
        if (new_room.room_type == "LR"):
            
            input_dir = "D:/AISGHackathonGitHub/hackathon_proj/media/room/images/" + file_str   # Change this as desired
            output_dir = "/Desktop/PeekingDuckOutput"  # Change this as desired

            # Initialise the nodes
            input_node = recorded.Node(input_dir=input_dir)
            efficientdet_node = efficientdet.Node(detect_ids=[14,61,62,63,66,71,84,85])
            dabble_bbox_count = bbox_count.Node()
            draw_node = bbox.Node(show_labels=True)
            
        
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            output_node = media_writer.Node(output_dir=output_dir)

            # Run it in the runner
            runner = Runner(nodes=[input_node, efficientdet_node, dabble_bbox_count,draw_node, output_node])
            runner.run()

            #Inspect the data
            count = runner.pipeline.data["count"]
            funitures = runner.pipeline.data["bbox_labels"]
                       

            print(count)
            print(funitures)


            funiture_array = []

            for f in funitures:
                if f not in funiture_array:
                    funiture_array.append(f)

            

            for fa in funiture_array:
                funiture_count = 0
                for fi in funitures:
                    if fi == fa:
                        funiture_count += 1

                Funiture.objects.create(room = new_room, object_name = fa, object_count = funiture_count)


            print(len(funiture_array))
            new_room.funiture_count = len(funiture_array)
            new_room.save()
        
        #peekingduck for Kitchen 
        elif (new_room.room_type == "KC"):

            input_dir = "D:/AISGHackathonGitHub/hackathon_proj/media/room/images/" + file_str   # Change this as desired
            output_dir = "/Desktop/PeekingDuckOutput"  # Change this as desired

            # Initialise the nodes
            input_node = recorded.Node(input_dir=input_dir)
            efficientdet_node = efficientdet.Node(detect_ids=[46,50,78,79,81,61,63,66])
            dabble_bbox_count = bbox_count.Node()
            draw_node = bbox.Node(show_labels=True)
            
        

            output_node = media_writer.Node(output_dir=output_dir)

            # Run it in the runner
            runner = Runner(nodes=[input_node, efficientdet_node, dabble_bbox_count,draw_node, output_node])
            runner.run()

            #Inspect the data
            count = runner.pipeline.data["count"]
            funitures = runner.pipeline.data["bbox_labels"]

            print(count)
            print(funitures)


            

            funiture_array = []

            for f in funitures:
                if f not in funiture_array:
                    funiture_array.append(f)

            

            for fa in funiture_array:
                funiture_count = 0
                for fi in funitures:
                    if fi == fa:
                        funiture_count += 1

                Funiture.objects.create(room = new_room, object_name = fa, object_count = funiture_count)


            print(len(funiture_array))
            new_room.funiture_count = len(funiture_array)
            new_room.save()

        #peekingduck for Room 
        elif (new_room.room_type == "R"):    

            input_dir = "D:/AISGHackathonGitHub/hackathon_proj/media/room/images/" + file_str   # Change this as desired
            output_dir = "/Desktop/PeekingDuckOutput"  # Change this as desired

            # Initialise the nodes
            input_node = recorded.Node(input_dir=input_dir)
            efficientdet_node = efficientdet.Node(detect_ids=[61,62,64,84,71,84,63])
            dabble_bbox_count = bbox_count.Node()
            draw_node = bbox.Node(show_labels=True)
            

            
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            output_node = media_writer.Node(output_dir=output_dir)

            # Run it in the runner
            runner = Runner(nodes=[input_node, efficientdet_node, dabble_bbox_count,draw_node, output_node])
            runner.run()

            #Inspect the data
            count = runner.pipeline.data["count"]
            funitures = runner.pipeline.data["bbox_labels"]

            print(count)
            print(funitures)
            

            funiture_array = []

            for f in funitures:
                if f not in funiture_array:
                    funiture_array.append(f)

            

            for fa in funiture_array:
                funiture_count = 0
                for fi in funitures:
                    if fi == fa:
                        funiture_count += 1

                Funiture.objects.create(room = new_room, object_name = fa, object_count = funiture_count)


            print(len(funiture_array))
            new_room.funiture_count = len(funiture_array)
            new_room.save()


        #rpa to retrieve peeking output image and add it to system 
        fileinputname = file_str.split(".")
        print(fileinputname[0])
        
        
        
        print(new_room.id)
        r.init(visual_automation = True, chrome_browser= False)
        r.wait(1)
        r.click('googleaddtab.png')
        r.wait(1)
        r.type('googlesearchbar.png', 'http://127.0.0.1:8000/dashboard/imageupdate/' + str(new_room.id) + "/" + '[enter]')
        r.wait(2)
        r.click('update.png')
        r.wait(1)
        r.keyboard('[ctrl][l]')
        r.wait(1)
        r.keyboard('D:\Desktop\PeekingDuckOutput[enter]')
        r.wait(1)
        r.type('fileexplorerselectfile.png',str(fileinputname[0]))
        r.wait(1)
        r.keyboard('[down][enter]')
        r.wait(1)
        r.click('buttontoupdate.png')
        r.wait(1)
    
        r.keyboard('[ctrl][w]')
        r.wait(1)
        r.click('googledashboardtab.png')
        r.close()
        
        return redirect('dashboard:add-rooms')

        


    
#to update funiture price 
class PriceEditView(LoginRequiredMixin, UpdateView): #to update a specific post
    model = Funiture
    fields = ['object_price']
    template_name = "price_edit.html"


    def post(self,request,pk,*args,**kwargs):
        funiture_o = Funiture.objects.get(id=pk)
        
        o_price = request.POST.get('object_price')
        
        funiture_o.object_price = o_price
      

        funiture_o.save()

    

        return redirect('dashboard:add-rooms')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        f_object = Funiture.objects.get(id=pk)
     
        context['f'] = f_object
     
        return context

#to update room image
class ImageEditView(LoginRequiredMixin, UpdateView):
    
    model = Room
    fields = ['image']
    template_name = "image_edit.html"


    def post(self,request,pk,*args,**kwargs):
        room = Room.objects.get(id=pk)
        
        r_image = request.FILES.getlist('image')

        print(r_image)
        

    

        for ri in r_image:
        
            room.image = ri
        

        room.save()

    

        return redirect('dashboard:add-rooms')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        room = Room.objects.get(id=pk)
     
        context['room'] = room
        context['form'] = UpdateImageForm()    
        return context


#get estimated funiture prices feature
class ExecuteRPA(LoginRequiredMixin, View): 

    
        # method to check if value is convertable to float
        def get(self,request,*args,**kwargs):
            
            def check_float(potential_float):
                try:
                    float(potential_float)
            
                    return True
                except ValueError:
                    return False
        

            # Get all room objects
            rooms = Room.objects.filter(user=request.user)

            
            print(rooms)

            
            for room in rooms:

                #get all funitures belong to that room
                funitures = room.funiture_set.all()
                theme = room.theme

                loop_counter = 0

                r.init(visual_automation = True, chrome_browser= False)
                r.wait(1)
                r.click('googleaddtab.png')
                r.type('googlesearchbar.png','https://shopping.google.com/?nord=1[enter]')
                
                for f in funitures:
                    print(f.object_name)

                    r.wait(1)

                    #rpa flow if is first funiture of the room
                    if (loop_counter == 0):

                        if (f.object_name == "tv" or f.object_name == "refrigerator" or f.object_name == "potted plant" or f.object_name == "clock" or f.object_name == "toaster" or f.object_name == "oven" or f.object_name == "vase"):
                            r.type('googleshoppingsearchbar.png', f.object_name + '[enter]')
                        else:
                            r.type('googleshoppingsearchbar.png', theme + " " + f.object_name + " " + '[enter]')

                       
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                   
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                       
                        r.keyboard('[down]')
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                   
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                     
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                  
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                     
                        r.keyboard('[down]')                        
                        r.keyboard('[down]')
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                  
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                     
                        r.keyboard('[down]')                        
                        r.keyboard('[down]')
                        r.keyboard('[down]')
                        
                        

                        

                        r.wait(1)
                        r.snap('page', 'D:/Desktop/output.png') #output.png is useless can delete
                        r.wait(2)
                        text = r.read('page.png')
                        

                        #to get estimate average price of funiture
                        words_array = text.split(" ")

                        print(words_array)
                    
                        value_array = []

                        for i in words_array:
                            if "$" in i:
                                print(i)
                                if "\n" in i:
                                    split_word = i.split("\n")

                                    for k in split_word:
                                        if "$" in k:
                                            if check_float(k[1:]):
                                                value_array.append(k[1:])

                                    print(split_word)
                                else:
                                    if check_float(i[1:]):
                                        value_array.append(i[1:])
                                
                        
                        print(value_array)

                        for va_item in value_array:
                            if float(va_item) > 10000:
                                value_array.remove(va_item)

                        total = 0
                        average = 0
                        for a in value_array:
                            total += float(a)

                        print(total) 
                        

                        average = total / len(value_array)

                        f.object_price = round(average, 2)
                        f.save()

                        print(average)

                        loop_counter = loop_counter + 1
                    
                    #rpa flow if is not the first funiture of the room
                    else:
                        r.hover(900, 300)
                        r.wait(1)
                        r.click("googlesearchremove.png")
                        r.wait(1)
                        
                        if (f.object_name == "tv" or f.object_name == "refrigerator" or f.object_name == "potted plant" or f.object_name == "clock" or f.object_name == "toaster" or f.object_name == "oven"  or f.object_name == "vase"):
                            
                            r.keyboard(f.object_name + '[enter]')
                            
                        else:
                            r.keyboard(theme + " " + f.object_name + " " + '[enter]')
                            

                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                   
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                       
                        r.keyboard('[down]')
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                   
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                     
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                  
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                     
                        r.keyboard('[down]')                        
                        r.keyboard('[down]')
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                  
                        r.keyboard('[down]')                      
                        r.keyboard('[down]')                     
                        r.keyboard('[down]')                        
                        r.keyboard('[down]')
                        r.keyboard('[down]')    
            
                        r.wait(1)
                        r.snap('page', 'D:/Desktop/output.png') #output.png is useless can delete
                        r.wait(1)
                        text2 = r.read('page.png')
                        
                        #to get estimate average price of funiture
                        words_array2 = text2.split(" ")

                        print(words_array2)
                    
                        value_array2 = []

                        for i2 in words_array2:
                            if "$" in i2:
                                if "\n" in i2:
                                    split_word2 = i2.split("\n")

                                    for k2 in split_word2:
                                        if "$" in k2:
                                            if check_float(k2[1:]):
                                                value_array2.append(k2[1:])

                                    print(split_word2)
                                else:
                                    if check_float(i2[1:]):
                                        value_array2.append(i2[1:])
                                
                        for va2_item in value_array2:
                            print(va2_item + "this is va2_item")
                            if float(va2_item) > 10000:
                                value_array2.remove(va2_item)

                        
                        print(value_array2)
                        total2 = 0
                        average2 = 0
                        for a2 in value_array2:
                            total2 += float(a2)

                        print(total2) 
                        

                        average2 = total2 / len(value_array2)

                        print(average2)

                        f.object_price = round(average2, 2)
                        f.save()

                        loop_counter = loop_counter + 1



                r.click('googledashboardtab.png')
                r.close()

            return redirect('dashboard:add-rooms')
       
        

 
    

