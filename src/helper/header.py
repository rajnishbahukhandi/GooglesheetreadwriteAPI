def common_header():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    return headers


def common_BearerTokenHeader():
    json_headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3IiwianRpIjoiZmEyM2M3OGI4NjU1MzgwYWVjMTA5NDQ1MzA1NDAxNDFmYjYwYjM1MWY5OWM4ZTYyNTQ4NTA3ODY3YzkwMTFlZDFkZGJiNjg5NmVkYTE1MjQiLCJpYXQiOjE2OTE4MzUzNzYuNTEwNjU1LCJuYmYiOjE2OTE4MzUzNzYuNTEwNjU4LCJleHAiOjE3MjM0NTc3NzYuNDkyNDQ4LCJzdWIiOiIyMjIiLCJzY29wZXMiOltdfQ.vFL-uEw8Zr-kCBARgSU0GZk2o7_S-EFrKW6Oy3d56AEBHYuGNDc6EY43xIJf_s8KDjdEM3kqp-yI4CDazx4Y7mp1-3v4jQQ42eeKywJnzW_xrv3cqVVM78rgi8BzwenWWbTUz1gDNHVyNCTyBZqL34lVxIs9hlcG5_2-KfZx-yaxxFvDWyDRG3Khhad674Nig4I2hVEmNZ9P85dfKrt5c2uscb4mWTyT7ELO0lgYt3AqOftBfgIrlQ6hFDVRU8J5qbEDHVUDiZYfHB8xM-x7fmbIlLLhWuK47GDuO1ELo-pYoqo3tdf7w6MMUREWlgppo1_-YknwTJCF6HszakJRYvemhElu_JJ7uGPCKuFFa1u3N_mxtYHP1RIp4199OxFnjgLXGUpyWbOnv1NJhN2pfamlQoOwwumHhoN22JS0UNPOSJ843MLtp2PNBb1gg20xEtqLnTD8N2N6-suznAooAHMa7Gg-st_Ctmw9Hqj2LQw6t_xaUG_AHb_X6m1PVCiMggO4HtVqtM6UhtmWSijMDUvgH2fqSu2EHbQCCG1MKtvpj6XMI4jJlEnz_3dmzOeu-Bb0lf8kam7hqCIJTWGrHswzgEOLh95QWVBtlnU1xZ3fROfOg-h59hiRwkuYTkUk4e9e2UgC18SgjRpjhUHl-8n1JV4i8BiZXYQu-wRS1IM'
    }
    return json_headers