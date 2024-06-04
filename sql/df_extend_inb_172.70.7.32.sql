SELECT
	call_date,
    phone_number_dialed,
    campaign_id,
    status,
    status_name,
    user,
    list_id,
    length_in_sec,
    lead_id,
    uniqueid,
    caller_code,
    IP_DESCARGA
FROM
    `bbdd_groupcos_repositorio_planta_telefonica`.`tb_marcaciones_vicidial_inb_172.70.7.32`
WHERE
    campaign_id IN ('AXA_AUTOS',
    'AXA_COLPATRIA',
    'AXAENDOSOS',
    'RETENSCOTI',
    'AXA_FIDEL',
    'AXA_FALABELLA',
    'AXA_SALUD',
    'AXA_FLAMINGO',
    'AXA_SOAT_SCOTIA',
    'IN_AXA_COLP')
        AND (call_date between CURRENT_TIMESTAMP() - INTERVAL 1 DAY and CURRENT_TIMESTAMP()) 