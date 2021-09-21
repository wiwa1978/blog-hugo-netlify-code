tenants = {
    "tenant1" = {
        tenant_name  = "tenant-1"
        tenant_description = "Tenant-1 description"
    }
    "tenant2" = {
        tenant_name  = "tenant-2"
        tenant_description = "Tenant-2 description"
    }
}

vrfs = {
    "tenant1" = {
        "vrf1" = {
            vrf_name  = "vrf_1_tenant_1"
        }
        "vrf2" = {
            vrf_name  = "vrf_2_tenant_1"
        }
    }
    "tenant2" = {
        "vrf3" = {
            vrf_name  = "vrf_3_tenant_2"
        }
        "vrf4" = {
            vrf_name  = "vrf_4_tenant_2"
        }
        "vrf5" = {
            vrf_name  = "vrf_5_tenant_2"
        }

    }
}

bds = {
    "tenant1"  =  {
        "bd1" = {
             bd_name = "bd_1_tenant_1"
             vrf = "vrf1"
        }
       
    }
    "tenant2"  =  {
        "bd2" = {
             bd_name = "bd_2_tenant_2"
             vrf = "vrf3"
        }
    }
}

aps = {
    "tenant1" = {
        "ap1" = {
            ap_name  = "application_profile_1_tenant_1"
        }
        "ap2" = {
            ap_name  = "application_profile_2_tenant_1"
        }
        "ap3" = {
            ap_name  = "application_profile_3_tenant_1"
        }
    }
    "tenant2" = {
        "ap7" = {
            ap_name  = "application_profile_7_tenant_2"
        }
        "ap4" = {
            ap_name  = "application_profile_4_tenant_2"
        }
        "ap3" = {
            ap_name  = "application_profile_3_tenant_2"
        }
    }
}


