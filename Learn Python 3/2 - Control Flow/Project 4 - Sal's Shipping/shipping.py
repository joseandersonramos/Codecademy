# Sal's Shipping project 🚚📦
# José Anderson Ramos Aquino 26/10/2023

# 1 - Ask the user for the weight of a package.
# 2 - Tell them the cheapest method of shipping.
# 3 - Tell them how much it'll cost.

print("🚚 Sal's Shippers📦\n")

weight = 41.5

print("⚖️ Weight of the package:", weight, "pound(s)\n")

# Ground Shipping
gs_cost = 0.00
gs_flat_charge = 20.00

if weight <= 2:
  gs_cost = weight * 1.5 + gs_flat_charge
elif weight > 2 and weight <= 6:
  gs_cost = weight * 3 + gs_flat_charge
elif weight > 6 and weight <= 10:
  gs_cost = weight * 4 + gs_flat_charge
else:
  gs_cost = weight * 4.75 + gs_flat_charge

print("Ground Shipping cost:", gs_cost) 

# Ground Shipping Premium
gsp_cost = 125.00

print("Ground Shipping Premium cost:",gsp_cost)

# Drone Shipping
ds_cost = 0

if weight <= 2:
  ds_cost = weight * 4.5
elif weight > 2 and weight <= 6:
  ds_cost = weight * 9
elif weight > 6 and weight <= 10:
  ds_cost = weight * 12
else:
  ds_cost = weight * 14.25

print("Drone Shipping cost:", ds_cost) 

# Cheapest method of shipping and how much it costs.

print("\n💵 The cheapest method of shipping is:")

if gs_cost < gsp_cost and gs_cost < ds_cost:
  print("\"🚚 Ground Shipping\":", gs_cost)
elif gsp_cost < gs_cost and gsp_cost < ds_cost:
  print("\"🚛 Ground Shipping Premium\":",gsp_cost)
else:
  print("\"🛩️ Drone Shipping\":", ds_cost)
