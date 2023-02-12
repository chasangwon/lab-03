# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
Done individually

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

RESTful API's can optimize client-server interactions thanks to statelessness. Statelessness eliminates the 
need to retain past client request information, reducing the load on the server. As a result, this leads
to scalability of RESTful API's.


Question 2: According to the definition of “resources” provided in the AWS article above,
What are the resources the mail server is providing to clients?

As the article defines it, resources are the information that different applications provide to their clients,
which can be in the form of text, images, videos, or etc. The mail server proviudes text containing information
requested by the client.


Question 3: What is one common REST Method not used in our mail server? How could
we extend our mail server to use this method?

The PUT request is not used in the current implementation of the mail server.The mail server can store drafts 
of emails that the user can later revise to complete the email. The user can update the contents of the
mail, such as recipient, subject, or body, by sending a PUT request.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they
serve? Make sure to cite any online resources you use to answer this question!

API keys provide project identification, identifying the application or 
or project that's making the call to the API, and project authorization, checking whether the calling 
application has been granted access to call the API. Some API's would want to use API keys to block anonymous
traffic, to control the number of calls made to the API, to keep track of usage patterns of the API, or
to filter logs by API key. 
https://cloud.google.com/endpoints/docs/openapi/when-why-api-key#:~:text=API%20keys%20provide%20project%20authorization,-To%20decide%20which&text=By%20identifying%20the%20calling%20project,or%20enabled%20in%20the%20API.  

...
