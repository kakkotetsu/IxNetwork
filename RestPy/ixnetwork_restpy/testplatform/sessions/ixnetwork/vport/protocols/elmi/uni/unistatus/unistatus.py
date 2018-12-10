
# Copyright 1997 - 2018 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
    
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class UniStatus(Base):
	"""The UniStatus class encapsulates a user managed uniStatus node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the UniStatus property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server using the find method.
	The internal properties list can be managed by the user by using the add and remove methods.
	"""

	_SDM_NAME = 'uniStatus'

	def __init__(self, parent):
		super(UniStatus, self).__init__(parent)

	@property
	def BwProfile(self):
		"""An instance of the BwProfile class.

		Returns:
			obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi.uni.unistatus.bwprofile.bwprofile.BwProfile)

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.elmi.uni.unistatus.bwprofile.bwprofile import BwProfile
		return BwProfile(self)

	@property
	def CeVlanIdEvcMapType(self):
		"""

		Returns:
			str(allToOneBundling|noBundling|bundling)
		"""
		return self._get_attribute('ceVlanIdEvcMapType')
	@CeVlanIdEvcMapType.setter
	def CeVlanIdEvcMapType(self, value):
		self._set_attribute('ceVlanIdEvcMapType', value)

	@property
	def Enabled(self):
		"""

		Returns:
			bool
		"""
		return self._get_attribute('enabled')
	@Enabled.setter
	def Enabled(self, value):
		self._set_attribute('enabled', value)

	@property
	def UniIdentifier(self):
		"""

		Returns:
			str
		"""
		return self._get_attribute('uniIdentifier')
	@UniIdentifier.setter
	def UniIdentifier(self, value):
		self._set_attribute('uniIdentifier', value)

	@property
	def UniIdentifierLength(self):
		"""

		Returns:
			number
		"""
		return self._get_attribute('uniIdentifierLength')
	@UniIdentifierLength.setter
	def UniIdentifierLength(self, value):
		self._set_attribute('uniIdentifierLength', value)

	def add(self, CeVlanIdEvcMapType=None, Enabled=None, UniIdentifier=None, UniIdentifierLength=None):
		"""Adds a new uniStatus node on the server and retrieves it in this instance.

		Args:
			CeVlanIdEvcMapType (str(allToOneBundling|noBundling|bundling)): 
			Enabled (bool): 
			UniIdentifier (str): 
			UniIdentifierLength (number): 

		Returns:
			self: This instance with all currently retrieved uniStatus data using find and the newly added uniStatus data available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._create(locals())

	def remove(self):
		"""Deletes all the uniStatus data in this instance from server.

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		self._delete()

	def find(self, CeVlanIdEvcMapType=None, Enabled=None, UniIdentifier=None, UniIdentifierLength=None):
		"""Finds and retrieves uniStatus data from the server.

		All named parameters support regex and can be used to selectively retrieve uniStatus data from the server.
		By default the find method takes no parameters and will retrieve all uniStatus data from the server.

		Args:
			CeVlanIdEvcMapType (str(allToOneBundling|noBundling|bundling)): 
			Enabled (bool): 
			UniIdentifier (str): 
			UniIdentifierLength (number): 

		Returns:
			self: This instance with matching uniStatus data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of uniStatus data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the uniStatus data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)