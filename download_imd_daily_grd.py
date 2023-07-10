import imdlib as imd



start_dy = '2020-07-07'
end_dy = '2020-07-09'
var_type = 'rain'         # other options are ('tmin'/ 'tmax')
file_dir='F:/imd_daily/rain/'
data = imd.get_real_data(var_type, start_dy, end_dy, file_dir)


