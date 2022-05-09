do_token    = "dop_v1_***"
domain_name = "wimwauters.com"
ssh_key     = "key_digitalocean_2020"

projects = {
  development = {
        description = "Description for Project Development"
        purpose     = "Web Application"
        environment = "Development"
        servers = {
          server1 = {
            name   = "Server1"
            size   = "s-2vcpu-2gb"
            image  = "ubuntu-21-10-x64"
            region = "ams3",
            tags   = ["web", "development"]
          }
      }
    },
    staging = {
        description = "Description for Project Staging"
        purpose     = "Service or API"
        environment = "Staging"
        servers = {
          server2 = {
            name   = "Server2"
            size   = "s-2vcpu-2gb"
            image  = "ubuntu-20-04-x64"
            region = "lon1",
            tags   = ["web", "staging"]
          },
          server3 = {
            name   = "Server3"
            size   = "s-2vcpu-2gb"
            image  = "ubuntu-20-04-x64"
            region = "lon1",
            tags   = ["web", "staging"]
        }
      }
    }
}



// companies = [
//   {
//     name        = "Company1"
//     description = "Description for company 1"
//     employees = [
//       {
//         name   = "Employee1"
//       }
//     ]
//   },
//   {
//     name        = "Company2"
//     description = "Description for company 2"
//     employees = [
//       {
//         name   = "Employee2"
//       },
//       {
//         name   = "Employee3"
//       }
//     ]
// }]

// locals {
//   nestedlist = flatten([
//     for company_key, company_value in var.companies : [
//       for employee_key, employee_value in company_value.employees : {
//         company_name        =   company_value.name
//         company_description =   company_value.description
//         employees           =   employee_value["name"]
//       }
//     ]
//   ])
// }


// flatten_output = [
//       + {
//           + company_description   = "Description for company 1"
//           + company_name          = "Company1"
//           + employees             = "Employee1"
//         },
//       + {
//           + company_description   = "Description for company 2"
//           + company_name          = "Company2"
//           + employees             = "Employee2"
//         },
//       + {
//           + company_description   = "Description for company 2"
//           + company_name          = "Company2"
//           + employees             = "Employee3"
//         },
//     ]


// flatten_output = [
//       + {
//           + company_description   = "Description for company 1"
//           + company_name          = "Company1"
//           + employees             = ["Employee1"]
//         },
//       + {
//           + company_description   = "Description for company 2"
//           + company_name          = "Company2"
//           + employees             = ["Employee2","Employee3"]
//         }
//     ]
