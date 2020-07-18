from course.models import  Course
from shop.settings import DATA_DIR
from os import listdir
from os.path import isfile, join, isdir
import yaml
from django.core.files import File

class CourseLoader(object):

    def __init__(self, *args, **kwargs):
        self.dir = args[0]

    def process(self):
        self.get_course_or_create()
        self.save_meta_course()

    def get_course_or_create(self):
        try:
            self.course = Course.objects.get(name_slug=self.dir)
        except:
            self.course = Course()
            self.course.name_slug = self.dir
            self.course.save()


    def save_meta_course(self):
        path = DATA_DIR+'/'+self.dir+'/meta.yml'
        print('Saving meta for %s' % self.course.name_slug)
        meta = self.get_meta(path)
        self.course.name = meta['title_ru']
        self.course.meta_keywords = meta['meta_keywords_ru']
        self.course.meta_title = meta['meta_title_ru']
        self.course.meta_description = meta['meta_description_ru']
        self.course.desc = meta['desc_ru']
        self.course.save()
        try:
            im_path = DATA_DIR + '/' + self.dir + '/image.png'
            print('Loading image %s' % im_path)
            with open(im_path, 'rb') as img_file:
                self.course.image.save('image.png', File(img_file), save=True)
        except Exception as e:
            print(str(e))

    


    def get_meta(self,path):
        if isfile(path):
            f = open(path,'r')
            str = f.read()
            f.close()
            yml = yaml.load(str, Loader=yaml.FullLoader)
            return yml
        else:
            return False

    @staticmethod
    def get_active_courses_dirs():
        out = []
        onlydirs = [f for f in listdir(DATA_DIR) if isdir(join(DATA_DIR, f))]
        for d in onlydirs:
            if d.find('.') == -1:
                out.append(d)
        return out


