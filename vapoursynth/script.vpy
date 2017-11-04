import vapoursynth as vs
import havsfunc as haf
core = vs.get_core()

#source
clip = core.lsmas.LWLibavSource(source="in.mkv")

#deinterlace
#clip = haf.QTGMC(clip, Preset="Very Slow",TFF=True)
#clip = core.std.SelectEvery(clip,cycle=2,offsets=0)

#crop
#clip = core.std.Crop(clip,left=2,right=2,top=22,bottom=22)

#deband
clip = core.f3kdb.Deband(clip,dither_algo=2,output_depth=10)

#subtitle
#clip = core.sub.TextFile(clip,file="in.ass")

#resize
clip = core.resize.Spline36(clip,1280,720)

#output
clip.set_output()