import network
import socket
import time
import machine
import rp2
  
from machine import Pin

amoxi = Pin(0, Pin.OUT) 
ibupro = Pin(1, Pin.OUT)
cetri = Pin(2, Pin.OUT)
paraceta = Pin(3, Pin.OUT)
asp = Pin(4, Pin.OUT)
vitad = Pin(5, Pin.OUT)
omeprazole = Pin(6, Pin.OUT)
prednisone = Pin(7, Pin.OUT)
ciprofloxacin = Pin(8, Pin.OUT)
metformin = Pin(9, Pin.OUT)
lisinopril = Pin(10, Pin.OUT)
simvastatin = Pin(11, Pin.OUT)
atorvastatin = Pin(12, Pin.OUT)
levothyroxine = Pin(13, Pin.OUT)
amlodipine = Pin(14, Pin.OUT)

board_led = machine.Pin('LED', machine.Pin.OUT)
board_led.off()

#WiFi SSID and password
ssid = 'SSID'            
password ='Password'

#Country name in 2 letters (India = IN)
rp2.country('IN')     

def connect():    #Function for connecting to Wi-Fi
    global wlan
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        time.sleep(2)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}') #Display IP addr

html = """
  <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <title>ARS</title>
    <style>
      h2 {
        text-align: center;
      }

      .card {
        transition: all 0.5s ease-in-out;
        cursor: pointer;
        box-shadow: 0px 0px 6px -4px rgba(0, 0, 0, 0.75);
        border-radius: 10px;
      }

      .card:hover {
        box-shadow: 0px 0px 51px -36px rgba(0, 0, 0, 1);
      }
    </style>
  </head>
  <body>
    <h1 class="text-center mt-2">ARS MEDICALS <img src="https://i.postimg.cc/QtvbhDhD/hospital-plus-icon-medical-health-symbol-vector-illustration-662353-370.webp" alt="Med symbol" style="width:90px;height:90px;">
    </h1>
    <h5 class="text-center mt-2">Opposite. Foodland Hotel, Nitte 574110</h5>
    <input type="text" class="form-control mt-3 mx-auto" id="myinput" placeholder="Search for medicines..." style="width:60%;">
    <div class="container mb-5">
      <h3 class="text-danger mt-5 text-center" id="para" style="display: none;">Not available </h3>
      <div class="row mt-3" id="card"></div>
    </div>
    <script>
      let filterArray = [];
      let galleryArray = [{
          id: 1,
          name: "Paracetamol",
          src: "https://5.imimg.com/data5/SELLER/Default/2022/11/UB/QV/LG/4619647/paracetamol-500-mg-tablets-500x500.jpeg",
          href: "/paraceta_led/on",
          desc: " "
        }, {
          id: 2,
          name: "Amoxicillin",
          src: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKPvctXZ9OK9jHacCTaShpsPEBsg6f1A3DYQ&usqp=CAU ",
          href: "/amoxi_led/on",
          desc: " "
        }, {
          id: 3,
          name: "Ibuprofen",
          src: "https://5.imimg.com/data5/QD/KO/MY-608147/untitled-2.jpg",
          href: "/ibupro_led/on",
          desc: " "
        }, {
          id: 4,
          name: "Cetrizine Hydrochloride",
          src: "https://www.adenhealthcare.com/wp-content/uploads/2018/07/CONIT-1.jpg",
          href: "/cetri_led/on",
          desc: " "
        }, {
          id: 5,
          name: "Aspirin",
          src: "https://image.made-in-china.com/202f0j00aqdlGmzBgDYg/Aspirin-Tablet-300mg-GMP-Drug.jpg",
          href: "/asp_led/on",
          desc: " "
        }, {
          id: 6,
          name: "Vitamin D",
          src: "https://www.netmeds.com/images/product-v1/600x600/891265/uprise_d3_60k_capsule_8s_0_1.jpg",
          href: "/vitad_led/on",
          desc: " "
        },
        // Add more medicines here
        {
          id: 7,
          name: "Omeprazole",
          src: "https://code1supply.com/assets/images/652087_ppkgleft.jpg",
          href: "/omeprazole_led/on",
          desc: " "
        }, {
          id: 8,
          name: "Prednisone",
          src: "https://c8.alamy.com/comp/KYH8H6/prednisolone-5mg-steroid-tablets-manufactured-by-c-p-pharmaceuticals-KYH8H6.jpg",
          href: "/prednisone_led/on",
          desc: " "
        }, {
          id: 9,
          name: "Ciprofloxacin",
          src: "https://assets3.drugcarts.com/category/product/cipcor-500mg-tablet.jpg",
          href: "/ciprofloxacin_led/on",
          desc: " "
        }, {
          id: 10,
          name: "Metformin",
          src: "https://5.imimg.com/data5/DT/TQ/GT/SELLER-107843500/metformin-tablets-500-mg.jpg",
          href: "/metformin_led/on",
          desc: " "
        }, {
          id: 11,
          name: "Lisinopril",
          src: "https://5.imimg.com/data5/SELLER/Default/2020/10/TC/IN/IF/26192048/lisinopril-tablet.jpg",
          href: "/lisinopril_led/on",
          desc: " "
        }, {
          id: 12,
          name: "Simvastatin",
          src: "https://5.imimg.com/data5/SELLER/Default/2023/4/302106874/LK/FS/LE/7034457/new-product-500x500.jpeg",
          href: "/simvastatin_led/on",
          desc: " "
        }, {
          id: 13,
          name: "Atorvastatin",
          src: "https://www.scottmorrison.in/wp-content/uploads/2022/07/LOWVAS-10.jpg",
          href: "/atorvastatin_led/on",
          desc: " "
        }, {
          id: 14,
          name: "Levothyroxine",
          src: "https://thyroiduk.org/wp-content/uploads/2023/02/Levothyroxine-T4.jpg",
          href: "/levothyroxine_led/on",
          desc: " "
        }, {
          id: 15,
          name: "Amlodipine",
          src: "https://www.albionbd.com/wp-content/uploads/2022/07/Amlodipine-5-Tablet.jpg",
          href: "/amlodipine_led/on",
          desc: " "
        }
      ];
      showGallery(galleryArray);

      function showGallery(currentArray) {
        document.getElementById("card").innerText = "";
        for (let i = 0; i < currentArray.length; i++) {
          document.getElementById("card").innerHTML += `
                    
										<div class="col-md-4 mt-3">
											<div class="card p-3 ps-5 pe-5">
												<h4 class="text-capitalize text-center">${currentArray[i].name}</h4>
												<img src="${currentArray[i].src}" width="100%" height="320px"/>
												<p class="mt-2">${currentArray[i].desc}</p>
												<a href="${currentArray[i].href}" class="btn btn-primary stretched-link w-100 mx-auto">Find</a>
											</div>
										</div>
                `;
        }
      }
      document.getElementById("myinput").addEventListener("keyup", function() {
        let text = this.value.toLowerCase();
        filterArray = galleryArray.filter(function(item) {
          return item.name.toLowerCase().includes(text);
        });
        if (this.value === "") {
          showGallery(galleryArray);
        } else {
          if (filterArray.length === 0) {
            document.getElementById("para").style.display = 'block';
            document.getElementById("card").innerHTML = "";
          } else {
            showGallery(filterArray);
            document.getElementById("para").style.display = 'none';
          }
        }
      });
    </script>
  </body>
</html>

"""
try:          #Attempt to connect to Wi-Fi
    connect()
    
except KeyboardInterrupt:
    board_led.off()
    time.sleep(1)
    machine.reset()
    
 
# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
 
s = socket.socket()
s.bind(addr)
s.listen(1)
time.sleep(2)
 
print('listening on', addr)
board_led.on()          #Turn on onboard LED once socket is opened
count = 0
 
# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)

        request = cl.recv(1024)
        print(request)         #Listening for 'GET' requests
        # Comparing GET requests. If a GET request is found, the 'request.find'
        # function stores the value after how many string values it is found
        # In this case, it is '6'. Otherwise, it will return '-1'
        request = str(request)
        amoxi_on = request.find('/amoxi_led/on')
        ibupro_on = request.find('/ibupro_led/on')
        cetri_on = request.find('/cetri_led/on')
        paraceta_on = request.find('/paraceta_led/on')
        asp_on = request.find('/asp_led/on')
        vitad_on = request.find('/vitad_led/on')
        omeprazole_on = request.find('/omeprazole_led/on')
        prednisone_on = request.find('/prednisone_led/on')
        ciprofloxacin_on = request.find('/ciprofloxacin_led/on')
        metformin_on = request.find('/metformin_led/on')
        lisinopril_on = request.find('/lisinopril_led/on')
        simvastatin_on = request.find('/simvastatin_led/on')
        atorvastatin_on = request.find('/atorvastatin_led/on')
        levothyroxine_on = request.find('/levothyroxine_led/on')
        amlodipine_on = request.find('/amlodipine_led/on')
         

        
        if count == 6: #This condition is implemented when LED is turned on
            count = 0
            time.sleep(1)
            amoxi.value(0)
            ibupro.value(0)
            cetri.value(0)
            paraceta.value(0)
            asp.value(0)
            vitad.value(0)
            omeprazole.value(0)
            prednisone.value(0)
            ciprofloxacin.value(0)
            metformin.value(0)
            lisinopril.value(0)
            simvastatin.value(0)
            atorvastatin.value(0)
            levothyroxine.value(0)
            amlodipine.value(0)
            print('Server is ready')
            
        if amoxi_on == 6:
           amoxi.value(1)
           time.sleep(1)
           count=count+1
        elif ibupro_on == 6:
             ibupro.value(1)
             time.sleep(1)
             count=count+1
        elif cetri_on == 6:
             cetri.value(1)
             time.sleep(1)
             count=count+1
        elif paraceta_on == 6:
             paraceta.value(1)
             time.sleep(1)
             count=count+1            
        elif asp_on == 6:
             asp.value(1)
             time.sleep(1)
             count=count+1
        elif vitad_on == 6:
             vitad.value(1)
             time.sleep(1)
             count=count+1
        elif omeprazole_on == 6:
             omeprazole.value(1)
             time.sleep(1)
             count=count+1
        elif prednisone_on == 6:
             prednisone.value(1)
             time.sleep(1)
             count=count+1
        elif ciprofloxacin_on == 6:
             ciprofloxacin.value(1)
             time.sleep(1)
             count=count+1
        elif metformin_on == 6:
             metformin.value(1)
             time.sleep(1)
             count=count+1
        elif lisinopril_on == 6:
             lisinopril.value(1)
             time.sleep(1)
             count=count+1
        elif simvastatin_on == 6:
             simvastatin.value(1)
             time.sleep(1)
             count=count+1
        elif atorvastatin_on == 6:
             atorvastatin.value(1)
             time.sleep(1)
             count=count+1
        elif levothyroxine_on == 6:
             levothyroxine.value(1)
             time.sleep(1)
             count=count+1
        elif amlodipine_on == 6:
             amlodipine.value(1)
             time.sleep(1)
             count=count+1
    

        

        
        response = html
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response) #Send response to the client
        cl.close()      #Close the connection
        print(f'{count}')
    except OSError as e:
        cl.close()
        print('connection closed')
