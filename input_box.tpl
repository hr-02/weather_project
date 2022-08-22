<html>
  <head>
	  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous">
	    <style>
		 .divider:after,
.divider:before {
content: "";
flex: 1;
height: 1px;
background: #eee;
}
.h-custom {
height: calc(100% - 73px);
}
@media (max-width: 450px) {
.h-custom {
height: 100%;
}
} 
.img-fluid
{
	height: 400px;
	
}
		</style>

  </head>
   
    <body>
		 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-pprn3073KE6tl6bjs2QrFaJGz5/SUsLqktiwsUTF55Jfv3qYSDhgCecCxMW52nD2" crossorigin="anonymous"></script>
		
		
		<br><br> 
  

<section class="vh-100">
  <div class="container-fluid h-custom">
    <div class="row d-flex justify-content-center align-items-center h-100">
      
      <div class="col-md-1 col-lg-1 col-xl-4">
        <img src="https://c.tenor.com/8cuueGbi6N0AAAAC/raining-rainy-weather.gif"
          class="img-fluid" alt="Sample image">
      </div>
      
      <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
        <form action="/login" method="post">
         

           <!-- Email input -->
          <div class="form-outline mb-4">
            <input name="precipitation" type="text" class="form-control form-control-lg"
              placeholder="Enter a precipitation " />
            <label class="form-label" for="form3Example3">Precipitation</label>
          </div>
          
          
          <div class="form-outline mb-4">
            <input name="temp_max" type="text"  class="form-control form-control-lg"
              placeholder="Enter Maximum Temperature" />
            <label class="form-label" for="form3Example3">Max Temperature</label>
          </div>
          

          <div class="form-outline mb-4">
            <input name="temp_min" type="text"  class="form-control form-control-lg"
              placeholder="Enter Minimum Temperature" />
            <label class="form-label" for="form3Example3">Min Temperature</label>
          </div>
          
           <div class="form-outline mb-4">
            <input name="wind" type="text"  class="form-control form-control-lg"
              placeholder="Enter wind" />
            <label class="form-label" for="form3Example3">Wind</label>
          </div>
          
          <div class="form-outline mb-4">
            <input name="weather" type="text" class="form-control form-control-lg"
              placeholder="Enter 0" />
            <label class="form-label" for="form3Example3">Weather</label>
          </div>

          

          <div class="text-center text-lg-start mt-4 pt-2">
            <button type="submit" class="btn btn-primary btn-lg"
            style="padding-left: 2.5rem; padding-right: 2.5rem;">submit</button>
            
          </div>

        </form>
      </div>
    </div>
  </div>

 
    </div>
    
  </div>
</section>



		

    </body>
    
    
    
    
    <!-- 
    
    
    
    <form action="/login" method="post">
		
		<br>
						
			Precipitation: <input name="precipitation" type="text" placeholder="numeric values" /><br>
			Max Temperature: <input name="temp_max" type="text" /><br>
			Min Temperature: <input name="temp_min" type="text" /><br>
			Wind: <input name="wind" type="text" /><br>
			Weather: <input name="weather" type="text" /><br>

			<input value="Update" type="submit" />
	
		</form>
		-->
</html>
