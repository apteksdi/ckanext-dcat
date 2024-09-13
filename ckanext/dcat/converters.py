from past.builtins import basestring
import logging

log = logging.getLogger(__name__)


def dcat_to_ckan(dcat_dict):

    package_dict = {}

    package_dict['title'] = dcat_dict.get('title')
    package_dict['notes'] = dcat_dict.get('description')
    package_dict['publisher_type'] = dcat_dict.get('publisher_type')
    package_dict['prioritas_tahun'] = dcat_dict.get('prioritas_tahun')
    package_dict['accessRights'] = dcat_dict.get('accessRights')
    package_dict['accrualPeriodicity'] = dcat_dict.get('accrualPeriodicity')
    package_dict['id_msind'] = dcat_dict.get('id_msind')
    package_dict['id_mskeg'] = dcat_dict.get('id_mskeg')
    package_dict['cara_pengumpulan_data'] = dcat_dict.get('cara_pengumpulan_data')
    package_dict['i_alamat'] = dcat_dict.get('i_alamat')
    package_dict['i_email'] = dcat_dict.get('i_email')
    package_dict['i_instansi_penyelanggara'] = dcat_dict.get('i_instansi_penyelanggara')
    package_dict['i_telepon'] = dcat_dict.get('i_telepon')
    package_dict['id_dds'] = dcat_dict.get('id_dds')
    package_dict['id_indikator_mms'] = dcat_dict.get('id_indikator_mms')
    package_dict['id_kegiatan'] = dcat_dict.get('id_kegiatan')
    package_dict['id_kegiatan_mms'] = dcat_dict.get('id_kegiatan_mms')
    package_dict['identitas_rekomendasi'] = dcat_dict.get('identitas_rekomendasi')
    package_dict['ii_pj_alamat'] = dcat_dict.get('ii_pj_alamat')
    package_dict['ii_pj_email'] = dcat_dict.get('ii_pj_email')
    package_dict['ii_pj_faksimile'] = dcat_dict.get('ii_pj_faksimile')
    package_dict['ii_pj_jabatan'] = dcat_dict.get('ii_pj_jabatan')
    package_dict['ii_pj_nama'] = dcat_dict.get('ii_pj_nama')
    package_dict['ii_pj_telepon'] = dcat_dict.get('ii_pj_telepon')
    package_dict['ii_unit_eselon1'] = dcat_dict.get('ii_unit_eselon1')
    package_dict['ii_unit_eselon2'] = dcat_dict.get('ii_unit_eselon2')
    package_dict['iii_latar_belakang_kegiatan'] = dcat_dict.get('iii_latar_belakang_kegiatang')
    package_dict['iii_tujuan_kegiatan'] = dcat_dict.get('iii_tujuan_kegiatan')
    package_dict['indikator_prioritas'] = dcat_dict.get('indikator_prioritas')
    package_dict['interpretasi'] = dcat_dict.get('interpretasi')
    package_dict['iv_cakupan_wilayah_pengumpulan_data'] = dcat_dict.get('iv_cakupan_wilayah_pengumpulan_data')
    package_dict['iv_frekuensi_penyelanggara'] = dcat_dict.get('iv_frekuensi_penyelanggara')
    package_dict['iv_kegiatan_ini_dilakukan'] = dcat_dict.get('iv_kegiatan_ini_dilakukan')
    package_dict['iv_metode_pengumpulan_data'] = dcat_dict.get('iv_metode_pengumpulan_data')
    package_dict['iv_sarana_pengumpulan_data'] = dcat_dict.get('iv_sarana_pengumpulan_data')
    package_dict['iv_tipe_pengumpulan_data'] = dcat_dict.get('iv_tipe_pengumpulan_data')
    package_dict['iv_unit_pengumpulan_data'] = dcat_dict.get('iv_unit_pengumpulan_data')
    package_dict['jenis'] = dcat_dict.get('jenis')
    package_dict['jenis_statistik'] = dcat_dict.get('jenis_statistik')
    package_dict['judul_kegiatan'] = dcat_dict.get('judul_kegiatan')
    package_dict['kodereferensi'] = dcat_dict.get('kodereferensi')
    package_dict['kriteria_prioritas'] = dcat_dict.get('kriteria_prioritas')
    package_dict['level_estimasi'] = dcat_dict.get('level_estimasi')
    package_dict['metode_perhitungan'] = dcat_dict.get('metode_perhitungan')
    package_dict['produsen_data_city_code'] = dcat_dict.get('produsen_data_city_code')
    package_dict['produsen_data_name'] = dcat_dict.get('produsen_data_name')
    package_dict['produsen_data_province_code'] = dcat_dict.get('produsen_data_province_code')
    package_dict['publishing_status'] = dcat_dict.get('publishing_status')
    package_dict['rumus'] = dcat_dict.get('rumus')
    package_dict['satuan'] = dcat_dict.get('satuan')
    package_dict['ukuran'] = dcat_dict.get('ukuran')
    package_dict['sektor_kegiatan'] = dcat_dict.get('sektor_kegiatan')
    package_dict['submission_period'] = dcat_dict.get('submission_period')
    package_dict['tahun_kegiatan'] = dcat_dict.get('tahun_kegiatan')
    package_dict['theme'] = dcat_dict.get('theme')
    package_dict['total_msind'] = dcat_dict.get('total_msind')
    package_dict['total_msvar'] = dcat_dict.get('total_msvar')
    package_dict['vi_apakah_melakukan_pelatihan_petugas'] = dcat_dict.get('vi_apakah_melakukan_pelatihan_petugas')
    package_dict['vi_apakah_melakukan_penyesuaian_nonrespon'] = dcat_dict.get('vi_apakah_melakukan_penyesuaian_nonrespon')
    package_dict['vi_apakah_melakukan_uji_coba'] = dcat_dict.get('vi_apakah_melakukan_uji_coba')
    package_dict['vi_jumlah_petugas_enumerator'] = dcat_dict.get('vi_jumlah_petugas_enumerator')
    package_dict['vi_jumlah_petugas_supervisor'] = dcat_dict.get('vi_jumlah_petugas_supervisor')
    package_dict['vi_metode_pemeriksaan_kualitas_pengumpulan_data'] = dcat_dict.get('vi_metode_pemeriksaan_kualitas_pengumpulan_data')
    package_dict['vii_metode_analisis'] = dcat_dict.get('vii_metode_analisis')
    package_dict['vii_tahapan_pengolahan_data'] = dcat_dict.get('vii_tahapan_pengolahan_data')
    package_dict['vii_tingkat_penyajian_hasil_analisis'] = dcat_dict.get('vii_tingkat_penyajian_hasil_analisis')
    package_dict['vii_unit_analisis'] = dcat_dict.get('vii_unit_analisis')
    package_dict['viii_ketersediaan_produk_digital'] = dcat_dict.get('viii_ketersediaan_produk_digital')
    package_dict['viii_ketersediaan_produk_mikrodata'] = dcat_dict.get('viii_ketersediaan_produk_mikrodata')
    package_dict['viii_ketersediaan_produk_tercetak'] = dcat_dict.get('viii_ketersediaan_produk_tercetak')
    
    package_dict['tags'] = []
    for keyword in dcat_dict.get('keyword', []):
        package_dict['tags'].append({'name': keyword})

    package_dict['extras'] = []
    for key in ['issued', 'modified']:
        package_dict['extras'].append({'key': 'dcat_{0}'.format(key), 'value': dcat_dict.get(key)})

        # package_dict['extras'].append({'key': 'publisher_type', 'value': dcat_dict.get('publisher_type')})

        # package_dict['extras'].append({'key': 'prioritas_tahun', 'value': dcat_dict.get('prioritas_tahun')})

        # package_dict['extras'].append({'key': 'accessRights', 'value': dcat_dict.get('accessRights')})

        # package_dict['extras'].append({'key': 'id_msind', 'value': dcat_dict.get('id_msind')})

        # package_dict['extras'].append({'key': 'id_mskeg', 'value': dcat_dict.get('id_mskeg')})

    package_dict['extras'].append({'key': 'guid', 'value': dcat_dict.get('identifier')})

    dcat_publisher = dcat_dict.get('publisher')
    if isinstance(dcat_publisher, basestring):
        package_dict['extras'].append({'key': 'dcat_publisher_name', 'value': dcat_publisher})
    elif isinstance(dcat_publisher, dict) and dcat_publisher.get('name'):
        package_dict['extras'].append({'key': 'dcat_publisher_name', 'value': dcat_publisher.get('name')})
        package_dict['extras'].append({'key': 'dcat_publisher_email', 'value': dcat_publisher.get('mbox')})

    package_dict['extras'].append({
        'key': 'language',
        'value': ','.join(dcat_dict.get('language', []))
    })

    package_dict['resources'] = []
    for distribution in dcat_dict.get('distribution', []):
        resource = {
            'name': distribution.get('title'),
            'description': distribution.get('description'),
            'url': distribution.get('downloadURL') or distribution.get('accessURL'),
            'format': distribution.get('format'),
        }

        if distribution.get('byteSize'):
            try:
                resource['size'] = int(distribution.get('byteSize'))
            except ValueError:
                pass
        package_dict['resources'].append(resource)

    return package_dict


def ckan_to_dcat(package_dict):

    dcat_dict = {}

    dcat_dict['title'] = package_dict.get('title')
    dcat_dict['description'] = package_dict.get('notes')
    dcat_dict['landingPage'] = package_dict.get('url')
    dcat_dict['publisher_type'] = package_dict.get('publisher_type')
    dcat_dict['prioritas_tahun'] = package_dict.get('prioritas_tahun')
    dcat_dict['accessRights'] = package_dict.get('accessRights')
    dcat_dict['accrualPeriodicity'] = package_dict.get('accrualPeriodicity')
    dcat_dict['id_msind'] = package_dict.get('id_msind')
    dcat_dict['id_mskeg'] = package_dict.get('id_mskeg')
    dcat_dict['cara_pengumpulan_data'] = package_dict.get('cara_pengumpulan_data')
    dcat_dict['i_alamat'] = package_dict.get('i_alamat')
    dcat_dict['i_email'] = package_dict.get('i_email')
    dcat_dict['i_instansi_penyelanggara'] = package_dict.get('i_instansi_penyelanggara')
    dcat_dict['i_telepon'] = package_dict.get('i_telepon')
    dcat_dict['id_dds'] = package_dict.get('id_dds')
    dcat_dict['id_indikator_mms'] = package_dict.get('id_indikator_mms')
    dcat_dict['id_kegiatan'] = package_dict.get('id_kegiatan')
    dcat_dict['id_kegiatan_mms'] = package_dict.get('id_kegiatan_mms')
    dcat_dict['identitas_rekomendasi'] = package_dict.get('identitas_rekomendasi')
    dcat_dict['ii_pj_alamat'] = package_dict.get('ii_pj_alamat')
    dcat_dict['ii_pj_email'] = package_dict.get('ii_pj_email')
    dcat_dict['ii_pj_faksimile'] = package_dict.get('ii_pj_faksimile')
    dcat_dict['ii_pj_jabatan'] = package_dict.get('ii_pj_jabatan')
    dcat_dict['ii_pj_nama'] = package_dict.get('ii_pj_nama')
    dcat_dict['ii_pj_telepon'] = package_dict.get('ii_pj_telepon')
    dcat_dict['ii_unit_eselon1'] = package_dict.get('ii_unit_eselon1')
    dcat_dict['ii_unit_eselon2'] = package_dict.get('ii_unit_eselon2')
    dcat_dict['iii_latar_belakang_kegiatan'] = package_dict.get('iii_latar_belakang_kegiatang')
    dcat_dict['iii_tujuan_kegiatan'] = package_dict.get('iii_tujuan_kegiatan')
    dcat_dict['indikator_prioritas'] = package_dict.get('indikator_prioritas')
    dcat_dict['interpretasi'] = package_dict.get('interpretasi')
    dcat_dict['iv_cakupan_wilayah_pengumpulan_data'] = package_dict.get('iv_cakupan_wilayah_pengumpulan_data')
    dcat_dict['iv_frekuensi_penyelanggara'] = package_dict.get('iv_frekuensi_penyelanggara')
    dcat_dict['iv_kegiatan_ini_dilakukan'] = package_dict.get('iv_kegiatan_ini_dilakukan')
    dcat_dict['iv_metode_pengumpulan_data'] = package_dict.get('iv_metode_pengumpulan_data')
    dcat_dict['iv_sarana_pengumpulan_data'] = package_dict.get('iv_sarana_pengumpulan_data')
    dcat_dict['iv_tipe_pengumpulan_data'] = package_dict.get('iv_tipe_pengumpulan_data')
    dcat_dict['iv_unit_pengumpulan_data'] = package_dict.get('iv_unit_pengumpulan_data')
    dcat_dict['jenis'] = package_dict.get('jenis')
    dcat_dict['jenis_statistik'] = package_dict.get('jenis_statistik')
    dcat_dict['judul_kegiatan'] = package_dict.get('judul_kegiatan')
    dcat_dict['kodereferensi'] = package_dict.get('kodereferensi')
    dcat_dict['kriteria_prioritas'] = package_dict.get('kriteria_prioritas')
    dcat_dict['level_estimasi'] = package_dict.get('level_estimasi')
    dcat_dict['metode_perhitungan'] = package_dict.get('metode_perhitungan')
    dcat_dict['produsen_data_city_code'] = package_dict.get('produsen_data_city_code')
    dcat_dict['produsen_data_name'] = package_dict.get('produsen_data_name')
    dcat_dict['produsen_data_province_code'] = package_dict.get('produsen_data_province_code')
    dcat_dict['publishing_status'] = package_dict.get('publishing_status')
    dcat_dict['rumus'] = package_dict.get('rumus')
    dcat_dict['satuan'] = package_dict.get('satuan')
    dcat_dict['ukuran'] = package_dict.get('ukuran')
    dcat_dict['sektor_kegiatan'] = package_dict.get('sektor_kegiatan')
    dcat_dict['submission_period'] = package_dict.get('submission_period')
    dcat_dict['tahun_kegiatan'] = package_dict.get('tahun_kegiatan')
    dcat_dict['theme'] = package_dict.get('theme')
    dcat_dict['total_msind'] = package_dict.get('total_msind')
    dcat_dict['total_msvar'] = package_dict.get('total_msvar')
    dcat_dict['vi_apakah_melakukan_pelatihan_petugas'] = package_dict.get('vi_apakah_melakukan_pelatihan_petugas')
    dcat_dict['vi_apakah_melakukan_penyesuaian_nonrespon'] = package_dict.get('vi_apakah_melakukan_penyesuaian_nonrespon')
    dcat_dict['vi_apakah_melakukan_uji_coba'] = package_dict.get('vi_apakah_melakukan_uji_coba')
    dcat_dict['vi_jumlah_petugas_enumerator'] = package_dict.get('vi_jumlah_petugas_enumerator')
    dcat_dict['vi_jumlah_petugas_supervisor'] = package_dict.get('vi_jumlah_petugas_supervisor')
    dcat_dict['vi_metode_pemeriksaan_kualitas_pengumpulan_data'] = package_dict.get('vi_metode_pemeriksaan_kualitas_pengumpulan_data')
    dcat_dict['vii_metode_analisis'] = package_dict.get('vii_metode_analisis')
    dcat_dict['vii_tahapan_pengolahan_data'] = package_dict.get('vii_tahapan_pengolahan_data')
    dcat_dict['vii_tingkat_penyajian_hasil_analisis'] = package_dict.get('vii_tingkat_penyajian_hasil_analisis')
    dcat_dict['vii_unit_analisis'] = package_dict.get('vii_unit_analisis')
    dcat_dict['viii_ketersediaan_produk_digital'] = package_dict.get('viii_ketersediaan_produk_digital')
    dcat_dict['viii_ketersediaan_produk_mikrodata'] = package_dict.get('viii_ketersediaan_produk_mikrodata')
    dcat_dict['viii_ketersediaan_produk_tercetak'] = package_dict.get('viii_ketersediaan_produk_tercetak')
    dcat_dict['keyword'] = []
    for tag in package_dict.get('tags', []):
        dcat_dict['keyword'].append(tag['name'])


    dcat_dict['publisher'] = {}

    for extra in package_dict.get('extras', []):
        if extra['key'] in ['dcat_issued', 'dcat_modified']:
            dcat_dict[extra['key'].replace('dcat_', '')] = extra['value']

        elif extra['key'] == 'language':
            dcat_dict['language'] = extra['value'].split(',')

        elif extra['key'] == 'dcat_publisher_name':
            dcat_dict['publisher']['name'] = extra['value']

        elif extra['key'] == 'dcat_publisher_email':
            dcat_dict['publisher']['mbox'] = extra['value']

        elif extra['key'] == 'guid':
            dcat_dict['identifier'] = extra['value']
        
        # elif extra['key'] == 'publisher_type':
        #     dcat_dict['publisher_type'] = extra['value']

        # elif extra['key'] == 'prioritas_tahun':
        #     dcat_dict['prioritas_tahun'] = extra['value']

        # elif extra['key'] == 'accessRights':
        #     dcat_dict['accessRights'] = extra['value']

        # elif extra['key'] == 'id_msind':
        #     dcat_dict['id_msind'] = extra['value']

        # elif extra['key'] == 'id_mskeg':
        #     dcat_dict['id_mskeg'] = extra['value']

    if not dcat_dict['publisher'].get('name') and package_dict.get('maintainer'):
        dcat_dict['publisher']['name'] = package_dict.get('maintainer')
        if package_dict.get('maintainer_email'):
            dcat_dict['publisher']['mbox'] = package_dict.get('maintainer_email')

    dcat_dict['distribution'] = []
    for resource in package_dict.get('resources', []):
        distribution = {
            'title': resource.get('name'),
            'description': resource.get('description'),
            'format': resource.get('format'),
            'byteSize': resource.get('size'),
            # TODO: downloadURL or accessURL depending on resource type?
            'accessURL': resource.get('url'),
        }
        dcat_dict['distribution'].append(distribution)

    return dcat_dict
