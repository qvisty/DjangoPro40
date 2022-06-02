# DjangoPro40
 My version of Django for Pros 4.0

chapter 15

+ added elephantsql Postgres
https://www.elephantsql.com/

**django-storages**
There are several steps that a truly production website could take but are beyond the current
scope of this book. The most important is storing all media files on a dedicated CDN (Content
Delivery Network) rather than on our own server. Unlike static files, which the developer controls
and can trust, media files are user-generated and should always be treated with caution. The
popular third-party package django-storages allows for storing Django media files on a service
like Amazon’s S3.
Furthermore the hosting service we will be using later on, Heroku, has an ephemeral file system.
Each internal dyno boots with a clean copy of the file system from the most recent deploy. Static
files are located on the file system; media files are not. As a result, in production media files
will not remain with Heroku. Using django-storages is therefore basically mandatory alongside
Heroku and will be mentioned again in the deployment chapter.

**Next Steps**
Additional steps could include extra validations on the image-uploading form to ensure that only
a normal, safe image was able to be added. We could add dedicated create/edit/delete forms for
the creation of books and cover image. Tests would be nice to have here too although they would
be primarily focused on the form validation section not the basic image-uploading via the admin.
Again this is an area that can become quite complex, but is worthy of further study.
The last recommendation is to look at the third-party django-cleanup package which automatically
deletes old files. It can be quite handy.