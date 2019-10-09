// validation scripts
// var reg = /[a-z]/ig;
// var reg2 = new RegExp(/[a-z]/, 'i');
"use strict";
const inputs = document.querySelectorAll('input');
const patterns = {
	a_email: /^([a-z\d\.-_]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/,
	agent_fname: /^[a-z]{2,25}$/i,
    agent_mname: /^[a-z]{1,25}$/i,
    agent_lname: /^[a-z]{2,25}$/i,
	agent_email: /^([a-z\d\.-_]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/,
	agent_mobile_no: /^(09|\+639)\d{9}$/,
    client_fname: /^[a-z]{2,25}$/i,
    client_mname: /^[a-z]{1,25}$/i,
    client_lname: /^[a-z]{2,25}$/i,
    client_profession: /^[a-z]{3,25}$/i,
    client_policy_no: /^[0-9]{7,11}$/,
    client_official_receipt_no: /^[0-9]{7}$/,
    client_plate_no: /^([A-Z]{2,3})\s+([0-9]{3,4})$/,
    client_chassis_no: /^[a-z0-9]{11}$/i,
    client_engine_no: /^[a-z0-9]{10}$/i,
    client_brand: /[a-zA-Z\d]{1,25}/,
    client_mv_file_no: /^[0-9]{10}$/,
    client_authorized_capacity: /^[0-9]{1,25}$/,
    client_unladen_weight: /^[0-9]{1,25}$/,
    telephone: /^\d{11}$/,
    a_username: /^[a-z\d]{5,12}$/i,
    a_password: /^[\w@-]{8,20}$/,
    slug: /^[a-z\d-]{8,20}$/,
    client_email: /^([a-z\d\.-_]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/
};

function validate(field, regex) {
    if(regex.test(field.value)){
        field.className = 'form-control valid';
    }
    else {
        field.className = 'form-control invalid';
    }
    console.log(regex.test(field.value));
}

inputs.forEach((input) => {
    input.addEventListener('keyup',(e) => {
        //console.log(e.target.attributes.name.value);
        validate(e.target, patterns[e.target.attributes.name.value]);
    });
});

$(':required').one('blur keydown', function() {
    $(this).addClass('touched');
});

function body_weight() {
	var e = document.getElementById("client_body");
	var client_car_body = e.options[e.selectedIndex].value;
	var weight = document.getElementById("client_unladen_weight").value;
	switch (client_car_body) {
		case "UV":
			weight = Math.ceil(weight/100)*100;
			if (weight >= 2700 || weight <= 4500 ){
				switch(weight){
					case 2700:
						var uv_total = document.getElementById("client_total_price").value = 2000;
					break;
					case 2800:
						var uv_total = document.getElementById("client_total_price").value = 2040;
					break;
					case 2900:
						var uv_total = document.getElementById("client_total_price").value = 2080;
					break;
					case 3000:
						var uv_total = document.getElementById("client_total_price").value = 2120;
					break;
					case 3100:
						var uv_total = document.getElementById("client_total_price").value = 2160;
					break;
					case 3200:
						var uv_total = document.getElementById("client_total_price").value = 2200;
					break;
					case 3300:
						var uv_total = document.getElementById("client_total_price").value = 2240;
					break;
					case 3400:
						var uv_total = document.getElementById("client_total_price").value = 2280;
					break;
					case 3500:
						var uv_total = document.getElementById("client_total_price").value = 2320;
					break;
					case 3600:
						var uv_total = document.getElementById("client_total_price").value = 2360;
					break;
					case 3700:
						var uv_total = document.getElementById("client_total_price").value = 2400;
					break;
					case 3800:
						var uv_total = document.getElementById("client_total_price").value = 2440;
					break;
					case 3900:
						var uv_total = document.getElementById("client_total_price").value = 2480;
					break;
					case 4000:
						var uv_total = document.getElementById("client_total_price").value = 2520;
					break;
					case 4100:
						var uv_total = document.getElementById("client_total_price").value = 2560;
					break;
					case 4200:
						var uv_total = document.getElementById("client_total_price").value = 2600;
					break;
					case 4300:
						var uv_total = document.getElementById("client_total_price").value = 2640;
					break;
					case 4400:
						var uv_total = document.getElementById("client_total_price").value = 2680;
					break;
					case 4500:
						var uv_total = document.getElementById("client_total_price").value = 2720;
					break;
					default:
						
				}
			}
			else {
				console.log("error uv");
			}
			break;
		case "Motorcycle":
			var motorcycle_total = document.getElementById("client_total_price").value = 240;
			break;
		case "Tricycle":
			var tricycle_total = document.getElementById("client_total_price").value = 300;
			break;
		case "Trailer":
			var trailer_total = document.getElementById("client_total_price").value = weight * 0.24;
			break;
		case "Car":
			weight = Math.ceil(weight/100)*100;
			if (weight < 1600 ) {
				var car_total = document.getElementById("client_total_price").value = 2000;
			}
			else if (weight >= 1600 && weight <= 2300) {
				car_total = document.getElementById("client_total_price").value = 6000;
			}
			else if (weight > 2300) {
				car_total = document.getElementById("client_total_price").value = 12000;
			}
			else {
				console.log("error car");
			}
			break;
		case "Truck":
		case "Bus":
			weight = Math.ceil(weight/100)*100;
			switch(weight) {
				case 4600:
				var truck_total = document.getElementById('client_total_price').value = 2255;
				break;
				case 4700:
				var truck_total = document.getElementById('client_total_price').value = 2280;
				break;
				case 4800:
				var truck_total = document.getElementById('client_total_price').value = 2305;
				break;
				case 4900:
				var truck_total = document.getElementById('client_total_price').value = 2330;
				break;
				case 5000:
				var truck_total = document.getElementById('client_total_price').value = 2350;
				break;
				case 5100:
				var truck_total = document.getElementById('client_total_price').value = 2375;
				break;
				case 5200:
				var truck_total = document.getElementById('client_total_price').value = 2400;
				break;
				case 5300:
				var truck_total = document.getElementById('client_total_price').value = 2425;
				break;
				case 5400:
				var truck_total = document.getElementById('client_total_price').value = 2450;
				break;
				case 5500:
				var truck_total = document.getElementById('client_total_price').value = 2470;
				break;
				case 5600:
				var truck_total = document.getElementById('client_total_price').value = 2495;
				break;
				case 5700:
				var truck_total = document.getElementById('client_total_price').value = 2520;
				break;
				case 5800:
				var truck_total = document.getElementById('client_total_price').value = 2545;
				break;
				case 5900:
				var truck_total = document.getElementById('client_total_price').value = 2570;
				break;
				case 6000:
				var truck_total = document.getElementById('client_total_price').value = 2590;
				break;
				case 6100:
				var truck_total = document.getElementById('client_total_price').value = 2615;
				break;
				case 6200:
				var truck_total = document.getElementById('client_total_price').value = 2640;
				break;
				case 6300:
				var truck_total = document.getElementById('client_total_price').value = 2665;
				break;
				case 6400:
				var truck_total = document.getElementById('client_total_price').value = 2690;
				break;
				case 6500:
				var truck_total = document.getElementById('client_total_price').value = 2710;
				break;
				case 6600:
				var truck_total = document.getElementById('client_total_price').value = 2735;
				break;
				case 6700:
				var truck_total = document.getElementById('client_total_price').value = 2760;
				break;
				case 6800:
				var truck_total = document.getElementById('client_total_price').value = 2785;
				break;
				case 6900:
				var truck_total = document.getElementById('client_total_price').value = 2810;
				break;
				case 7000:
				var truck_total = document.getElementById('client_total_price').value = 2830;
				break;
				case 7100:
				var truck_total = document.getElementById('client_total_price').value = 2855;
				break;
				case 7200:
				var truck_total = document.getElementById('client_total_price').value = 2880;
				break;
				case 7300:
				var truck_total = document.getElementById('client_total_price').value = 2905;
				break;
				case 7400:
				var truck_total = document.getElementById('client_total_price').value = 2930;
				break;
				case 7500:
				var truck_total = document.getElementById('client_total_price').value = 2950;
				break;
				case 7600:
				var truck_total = document.getElementById('client_total_price').value = 2975;
				break;
				case 7700:
				var truck_total = document.getElementById('client_total_price').value = 3000;
				break;
				case 7800:
				var truck_total = document.getElementById('client_total_price').value = 3025;
				break;
				case 7900:
				var truck_total = document.getElementById('client_total_price').value = 3050;
				break;
				case 8000:
				var truck_total = document.getElementById('client_total_price').value = 3070;
				break;
				case 8100:
				var truck_total = document.getElementById('client_total_price').value = 3095;
				break;
				case 8200:
				var truck_total = document.getElementById('client_total_price').value = 3120;
				break;
				case 8300:
				var truck_total = document.getElementById('client_total_price').value = 3145;
				break;
				case 8400:
				var truck_total = document.getElementById('client_total_price').value = 3170;
				break;
				case 8500:
				var truck_total = document.getElementById('client_total_price').value = 3190;
				break;
				case 8600:
				var truck_total = document.getElementById('client_total_price').value = 3215;
				break;
				case 8700:
				var truck_total = document.getElementById('client_total_price').value = 3240;
				break;
				case 8800:
				var truck_total = document.getElementById('client_total_price').value = 3265;
				break;
				case 8900:
				var truck_total = document.getElementById('client_total_price').value = 3290;
				break;
				case 9000:
				var truck_total = document.getElementById('client_total_price').value = 3310;
				break;
				case 9100:
				var truck_total = document.getElementById('client_total_price').value = 3335;
				break;
				case 9200:
				var truck_total = document.getElementById('client_total_price').value = 3360;
				break;
				case 9300:
				var truck_total = document.getElementById('client_total_price').value = 3385;
				break;
				case 9400:
				var truck_total = document.getElementById('client_total_price').value = 3410;
				break;
				case 9500:
				var truck_total = document.getElementById('client_total_price').value = 3430;
				break;
				case 9600:
				var truck_total = document.getElementById('client_total_price').value = 3455;
				break;
				case 9700:
				var truck_total = document.getElementById('client_total_price').value = 3480;
				break;
				case 9800:
				var truck_total = document.getElementById('client_total_price').value = 3505;
				break;
				case 9900:
				var truck_total = document.getElementById('client_total_price').value = 3530;
				break;
				case 10000:
				var truck_total = document.getElementById('client_total_price').value = 3550;
				break;
				case 10100:
				var truck_total = document.getElementById('client_total_price').value = 3575;
				break;
				case 10200:
				var truck_total = document.getElementById('client_total_price').value = 3600;
				break;
				case 10300:
				var truck_total = document.getElementById('client_total_price').value = 3625;
				break;
				case 10400:
				var truck_total = document.getElementById('client_total_price').value = 3650;
				break;
				case 10500:
				var truck_total = document.getElementById('client_total_price').value = 3670;
				break;
				case 10600:
				var truck_total = document.getElementById('client_total_price').value = 3695;
				break;
				case 10700:
				var truck_total = document.getElementById('client_total_price').value = 3720;
				break;
				case 10800:
				var truck_total = document.getElementById('client_total_price').value = 3745;
				break;
				case 10900:
				var truck_total = document.getElementById('client_total_price').value = 3770;
				break;
				case 11000:
				var truck_total = document.getElementById('client_total_price').value = 3790;
				break;
				case 11100:
				var truck_total = document.getElementById('client_total_price').value = 3815;
				break;
				case 11200:
				var truck_total = document.getElementById('client_total_price').value = 3840;
				break;
				case 11300:
				var truck_total = document.getElementById('client_total_price').value = 3865;
				break;
				case 11400:
				var truck_total = document.getElementById('client_total_price').value = 3890;
				break;
				case 11500:
				var truck_total = document.getElementById('client_total_price').value = 3910;
				break;
				case 11600:
				var truck_total = document.getElementById('client_total_price').value = 3935;
				break;
				case 11700:
				var truck_total = document.getElementById('client_total_price').value = 3960;
				break;
				case 11800:
				var truck_total = document.getElementById('client_total_price').value = 3985;
				break;
				case 11900:
				var truck_total = document.getElementById('client_total_price').value = 4010;
				break;
				case 12000:
				var truck_total = document.getElementById('client_total_price').value = 4030;
				break;
				case 12100:
				var truck_total = document.getElementById('client_total_price').value = 4055;
				break;
				case 12200:
				var truck_total = document.getElementById('client_total_price').value = 4080;
				break;
				case 12300:
				var truck_total = document.getElementById('client_total_price').value = 4105;
				break;
				case 12400:
				var truck_total = document.getElementById('client_total_price').value = 4130;
				break;
				case 12500:
				var truck_total = document.getElementById('client_total_price').value = 4150;
				break;
				case 12600:
				var truck_total = document.getElementById('client_total_price').value = 4175;
				break;
				case 12700:
				var truck_total = document.getElementById('client_total_price').value = 4200;
				break;
				case 12800:
				var truck_total = document.getElementById('client_total_price').value = 4225;
				break;
				case 12900:
				var truck_total = document.getElementById('client_total_price').value = 4250;
				break;
				case 13000:
				var truck_total = document.getElementById('client_total_price').value = 4270;
				break;
				case 13100:
				var truck_total = document.getElementById('client_total_price').value = 4295;
				break;
				case 13200:
				var truck_total = document.getElementById('client_total_price').value = 4320;
				break;
				case 13300:
				var truck_total = document.getElementById('client_total_price').value = 4345;
				break;
				case 13400:
				var truck_total = document.getElementById('client_total_price').value = 4370;
				break;
				case 13500:
				var truck_total = document.getElementById('client_total_price').value = 4390;
				break;
				case 13600:
				var truck_total = document.getElementById('client_total_price').value = 4415;
				break;
				case 13700:
				var truck_total = document.getElementById('client_total_price').value = 4440;
				break;
				case 13800:
				var truck_total = document.getElementById('client_total_price').value = 4465;
				break;
				case 13900:
				var truck_total = document.getElementById('client_total_price').value = 4490;
				break;
				case 14000:
				var truck_total = document.getElementById('client_total_price').value = 4510;
				break;
				case 14100:
				var truck_total = document.getElementById('client_total_price').value = 4535;
				break;
				case 14200:
				var truck_total = document.getElementById('client_total_price').value = 4560;
				break;
				case 14300:
				var truck_total = document.getElementById('client_total_price').value = 4585;
				break;
				case 14400:
				var truck_total = document.getElementById('client_total_price').value = 4610;
				break;
				case 14500:
				var truck_total = document.getElementById('client_total_price').value = 4630;
				break;
				case 14600:
				var truck_total = document.getElementById('client_total_price').value = 4655;
				break;
				case 14700:
				var truck_total = document.getElementById('client_total_price').value = 4680;
				break;
				case 14800:
				var truck_total = document.getElementById('client_total_price').value = 4705;
				break;
				case 14900:
				var truck_total = document.getElementById('client_total_price').value = 4730;
				break;
				case 15000:
				var truck_total = document.getElementById('client_total_price').value = 4750;
				break;
				case 15100:
				var truck_total = document.getElementById('client_total_price').value = 4775;
				break;
				case 15200:
				var truck_total = document.getElementById('client_total_price').value = 4800;
				break;
				case 15300:
				var truck_total = document.getElementById('client_total_price').value = 4825;
				break;
				case 15400:
				var truck_total = document.getElementById('client_total_price').value = 4850;
				break;
				case 15500:
				var truck_total = document.getElementById('client_total_price').value = 4870;
				break;
				case 15600:
				var truck_total = document.getElementById('client_total_price').value = 4895;
				break;
				case 15700:
				var truck_total = document.getElementById('client_total_price').value = 4920;
				break;
				case 15800:
				var truck_total = document.getElementById('client_total_price').value = 4945;
				break;
				case 15900:
				var truck_total = document.getElementById('client_total_price').value = 4970;
				break;
				case 16000:
				var truck_total = document.getElementById('client_total_price').value = 4990;
				break;
				case 16100:
				var truck_total = document.getElementById('client_total_price').value = 5015;
				break;
				case 16200:
				var truck_total = document.getElementById('client_total_price').value = 5040;
				break;
				case 16300:
				var truck_total = document.getElementById('client_total_price').value = 5065;
				break;
				case 16400:
				var truck_total = document.getElementById('client_total_price').value = 5090;
				break;
				case 16500:
				var truck_total = document.getElementById('client_total_price').value = 5110;
				break;
				case 16600:
				var truck_total = document.getElementById('client_total_price').value = 5135;
				break;
				case 16700:
				var truck_total = document.getElementById('client_total_price').value = 5160;
				break;
				case 16800:
				var truck_total = document.getElementById('client_total_price').value = 5185;
				break;
				case 16900:
				var truck_total = document.getElementById('client_total_price').value = 5210;
				break;
				case 17000:
				var truck_total = document.getElementById('client_total_price').value = 5230;
				break;
				case 17100:
				var truck_total = document.getElementById('client_total_price').value = 5255;
				break;
				case 17200:
				var truck_total = document.getElementById('client_total_price').value = 5280;
				break;
				case 17300:
				var truck_total = document.getElementById('client_total_price').value = 5305;
				break;
				case 17400:
				var truck_total = document.getElementById('client_total_price').value = 5330;
				break;
				case 17500:
				var truck_total = document.getElementById('client_total_price').value = 5350;
				break;
				case 17600:
				var truck_total = document.getElementById('client_total_price').value = 5375;
				break;
				case 17700:
				var truck_total = document.getElementById('client_total_price').value = 5400;
				break;
				case 17800:
				var truck_total = document.getElementById('client_total_price').value = 5425;
				break;
				case 17900:
				var truck_total = document.getElementById('client_total_price').value = 5450;
				break;
				case 18000:
				var truck_total = document.getElementById('client_total_price').value = 5470;
				break;
				case 18100:
				var truck_total = document.getElementById('client_total_price').value = 5495;
				break;
				case 18200:
				var truck_total = document.getElementById('client_total_price').value = 5520;
				break;
				case 18300:
				var truck_total = document.getElementById('client_total_price').value = 5545;
				break;
				case 18400:
				var truck_total = document.getElementById('client_total_price').value = 5570;
				break;
				case 18500:
				var truck_total = document.getElementById('client_total_price').value = 5590;
				break;
				case 18600:
				var truck_total = document.getElementById('client_total_price').value = 5615;
				break;
				case 18700:
				var truck_total = document.getElementById('client_total_price').value = 5640;
				break;
				case 18800:
				var truck_total = document.getElementById('client_total_price').value = 5665;
				break;
				case 18900:
				var truck_total = document.getElementById('client_total_price').value = 5690;
				break;
				case 19000:
				var truck_total = document.getElementById('client_total_price').value = 5710;
				break;
				case 19100:
				var truck_total = document.getElementById('client_total_price').value = 5735;
				break;
				case 19200:
				var truck_total = document.getElementById('client_total_price').value = 5760;
				break;
				case 19300:
				var truck_total = document.getElementById('client_total_price').value = 5785;
				break;
				case 19400:
				var truck_total = document.getElementById('client_total_price').value = 5810;
				break;
				case 19500:
				var truck_total = document.getElementById('client_total_price').value = 5830;
				break;
				case 19600:
				var truck_total = document.getElementById('client_total_price').value = 5855;
				break;
				case 19700:
				var truck_total = document.getElementById('client_total_price').value = 5880;
				break;
				case 19800:
				var truck_total = document.getElementById('client_total_price').value = 5905;
				break;
				case 19900:
				var truck_total = document.getElementById('client_total_price').value = 5930;
				break;
				case 20000:
				var truck_total = document.getElementById('client_total_price').value = 5950;
				break;
				case 20100:
				var truck_total = document.getElementById('client_total_price').value = 5975;
				break;
				case 20200:
				var truck_total = document.getElementById('client_total_price').value = 6000;
				break;
				case 20300:
				var truck_total = document.getElementById('client_total_price').value = 6025;
				break;
				case 20400:
				var truck_total = document.getElementById('client_total_price').value = 6050;
				break;
				case 20500:
				var truck_total = document.getElementById('client_total_price').value = 6070;
				break;
				case 20600:
				var truck_total = document.getElementById('client_total_price').value = 6095;
				break;
				case 20700:
				var truck_total = document.getElementById('client_total_price').value = 6120;
				break;
				case 20800:
				var truck_total = document.getElementById('client_total_price').value = 6145;
				break;
				case 20900:
				var truck_total = document.getElementById('client_total_price').value = 6170;
				break;
				case 21000:
				var truck_total = document.getElementById('client_total_price').value = 6190;
				break;
				case 21100:
				var truck_total = document.getElementById('client_total_price').value = 6215;
				break;
				case 21200:
				var truck_total = document.getElementById('client_total_price').value = 6240;
				break;
				case 21300:
				var truck_total = document.getElementById('client_total_price').value = 6265;
				break;
				case 21400:
				var truck_total = document.getElementById('client_total_price').value = 6290;
				break;
				case 21500:
				var truck_total = document.getElementById('client_total_price').value = 6310;
				break;
				case 21600:
				var truck_total = document.getElementById('client_total_price').value = 6335;
				break;
				case 21700:
				var truck_total = document.getElementById('client_total_price').value = 6360;
				break;
				case 21800:
				var truck_total = document.getElementById('client_total_price').value = 6385;
				break;
				case 21900:
				var truck_total = document.getElementById('client_total_price').value = 6410;
				break;
				case 22000:
				var truck_total = document.getElementById('client_total_price').value = 6430;
				break;
				case 22100:
				var truck_total = document.getElementById('client_total_price').value = 6455;
				break;
				case 22200:
				var truck_total = document.getElementById('client_total_price').value = 6480;
				break;
				case 22300:
				var truck_total = document.getElementById('client_total_price').value = 6505;
				break;
				case 22400:
				var truck_total = document.getElementById('client_total_price').value = 6530;
				break;
				case 22500:
				var truck_total = document.getElementById('client_total_price').value = 6550;
				break;
				case 22600:
				var truck_total = document.getElementById('client_total_price').value = 6575;
				break;
				case 22700:
				var truck_total = document.getElementById('client_total_price').value = 6600;
				break;
				case 22800:
				var truck_total = document.getElementById('client_total_price').value = 6625;
				break;
				case 22900:
				var truck_total = document.getElementById('client_total_price').value = 6650;
				break;
				case 23000:
				var truck_total = document.getElementById('client_total_price').value = 6670;
				break;
				case 23100:
				var truck_total = document.getElementById('client_total_price').value = 6695;
				break;
				case 23200:
				var truck_total = document.getElementById('client_total_price').value = 6720;
				break;
				case 23300:
				var truck_total = document.getElementById('client_total_price').value = 6745;
				break;
				case 23400:
				var truck_total = document.getElementById('client_total_price').value = 6770;
				break;
				case 23500:
				var truck_total = document.getElementById('client_total_price').value = 6790;
				break;
				case 23600:
				var truck_total = document.getElementById('client_total_price').value = 6815;
				break;
				case 23700:
				var truck_total = document.getElementById('client_total_price').value = 6840;
				break;
				case 23800:
				var truck_total = document.getElementById('client_total_price').value = 6865;
				break;
				case 23900:
				var truck_total = document.getElementById('client_total_price').value = 6890;
				break;
				case 24000:
				var truck_total = document.getElementById('client_total_price').value = 6910;
				break;
				case 24100:
				var truck_total = document.getElementById('client_total_price').value = 6935;
				break;
				case 24200:
				var truck_total = document.getElementById('client_total_price').value = 6960;
				break;
				case 24300:
				var truck_total = document.getElementById('client_total_price').value = 6985;
				break;
				case 24400:
				var truck_total = document.getElementById('client_total_price').value = 7010;
				break;
				case 24500:
				var truck_total = document.getElementById('client_total_price').value = 7030;
				break;
				case 24600:
				var truck_total = document.getElementById('client_total_price').value = 7055;
				break;
				case 24700:
				var truck_total = document.getElementById('client_total_price').value = 7080;
				break;
				case 24800:
				var truck_total = document.getElementById('client_total_price').value = 7105;
				break;
				case 24900:
				var truck_total = document.getElementById('client_total_price').value = 7130;
				break;	
			}
			break;
		default:
    		console.log("error cars");
		
	}
}
