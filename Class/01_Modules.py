'''
मोड्युलहरू (Modules)
मोड्युल भनेको एउटा पाइथन फाइल हो जसमा फङ्क्सनहरू, क्लासहरू, 
र चरहरू हुन्छन्। यसले हामीलाई हाम्रो कोडलाई व्यवस्थित गर्न र पुन: प्रयोग गर्न मद्दत गर्छ।

'''
import math

# a = math.sqrt(100)

# print(a)

# # माथिको कोडमा, math मोड्युललाई आयात गरिएको छ। यो मोड्युलमा धेरै गणितीय फङ्क्सनहरू हुन्छन्।

numbers = range(5, 10)  # This creates a range of numbers from 1 to 4
result = math.prod(numbers)
print(result)  # Output: 24