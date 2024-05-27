//signup successful
window.onload = function () {
  var pValue = document.querySelector("p").textContent;

  //LOGIN
  //login successful
  if (pValue.trim() === "login") {
    alert("Login Successful.");
    window.location.href = "/dashboard";
  }
  //login unsuccessful
  else if (pValue.trim() === "loginuns") {
    alert("Login Unsuccessful.\nPlease Try Again.");
    window.location.href = "/login";
  }

  //SIGNUP
  //signup successful
  else if (pValue.trim() === "signup") {
    alert("Sign Up Successful.");
    window.location.href = "/login";
  }
  //signout successful
  else if (pValue.trim() === "signout") {
    alert("Sign Out Successful.");
    window.location.href = "/";
  }
  //password not matched
  else if (pValue.trim() === "pwdnomatch") {
    alert("Passwords Didn't Match.\nPlease Try Again..");
    window.location.href = "/signup";
  }

  //SERVER
  //server errors
  else if (pValue.trim() === "server") {
    alert("Server Error Occured.\nPlease Try Again..");
    window.location.href = "/";
  }
  //database connection failed
  else if (pValue.trim() === "serverdb") {
    alert("Couldn't Connect Database.\nPlease Try Again..");
    window.location.href = "/";
  }
  //django raised an error
  else if (pValue.trim() === "django") {
    alert("DJango Error.\nPlease Try Again..");
    window.location.href = "/";
  }

  //ADDITION
  //contact added
  else if (pValue.trim() === "add") {
    alert("Contact Added Successful.");
    window.location.href = "/dashboard";
  }
  //contact was not added
  else if (pValue.trim() === "adduns") {
    alert("Couldn't Add Contact.\n Please Try Again.");
    window.location.href = "/add";
  }
  //repeated contact
  else if (pValue.trim() === "repeat") {
    alert("This Contact is Already Present.");
    window.location.href = "/dashboard";
  }

  //DELETION
  //deleted contact successfully
  else if (pValue.trim() === "deleted") {
    alert("Contact Deleted Successfully.");
    window.location.href = "/dashboard";
  }
  //no contact to delete
  else if (pValue.trim() === "nocontact") {
    alert("No Contact Present with the\ngiven Name or Contact No.!!.");
    window.location.href = "/dashboard";
  }
  //no data given in form
  else if (pValue.trim() === "nodatatodel") {
    alert("Please Give First Name or Contact Number\nto Delete");
    window.location.href = "/dashboard";
  }
  //deleted contact successfully
  else if (pValue.trim() === "deleted") {
    alert("Contact Deleted Successfully.");
    window.location.href = "/dashboard";
  }

  //SEARCHING
  //no data given in form
  else if (pValue.trim() === "nodatatosearchl") {
    alert("Please Give First Name or Contact Number\nto Search.");
    window.location.href = "/dashboard";
  }

  //UPDATING
  //update successful
  else if (pValue.trim() === "updatesuc") {
    alert("Profile Updated Successfully.");
    window.location.href = "/dashboard";
  }
  //update unsuccessful
  else if (pValue.trim() === "updateuns") {
    alert("Couldn't Update Profile\nPlease Try Again.");
    window.location.href = "/update";
  }
  //new old passwords didnt match
  else if (pValue.trim() === "pwdnomatch") {
    alert("Password Didn't Match\nPlease Try Again.");
    window.location.href = "/update";
  }
  //old password wrong
  else if (pValue.trim() === "oldpwdwrong") {
    alert("Password Didn't Match\nPlease Try Again.");
    window.location.href = "/update";
  }
  //no data to update
  else if (pValue.trim() === "nodatatoupdate") {
    alert("Please Fill all Data Fields to Update Profile.");
    window.location.href = "/dashboard";
  }
};
